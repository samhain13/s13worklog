from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    @property
    def tasks(self):
        return self.task_set.all()

    @property
    def tasks_doing(self):
        return self.task_set.filter(done=False)

    @property
    def tasks_done(self):
        return self.task_set.filter(done=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    categories = models.ManyToManyField(
        Category
    )
    done = models.BooleanField(
        default=False
    )
    users = models.ManyToManyField(
        User,
        verbose_name='Assigned Users'
    )

    @property
    def logs(self):
        return self.logitem_set.all()

    def __str__(self):
        return self.name

    def get_user_logs(self, user):
        return self.logitem_set.filter(owner=user)


class LogItem(models.Model):
    start_dt = models.DateTimeField(
        verbose_name='Start Date and Time'
    )
    end_dt = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='End Date and Time'
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    notes = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['owner', 'start_dt']
        verbose_name = 'Log Item'
        verbose_name_plural = 'Log Items'

    def __str__(self):
        return '{} - {} by {}'.format(
            str(self.task),
            self.start_dt.strftime('%Y-%m-%d %H:%M'),
            self.owner.username
        )

    def save(self, *args, **kwargs):
        # Sanity checks.
        if self.start_dt and self.end_dt:
            if self.end_dt < self.start_dt:
                raise ValidationError(
                    'End date-time cannot come before start date-time.')
        return super(LogItem, self).save(*args, **kwargs)
