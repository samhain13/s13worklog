from django.core.exceptions import ValidationError
from django.db import models


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )


class LogItem(models.Model):
    start_dt = models.DateTimeField(
        null=True,
        blank=True,
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
    notes = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Log Item'
        verbose_name_plural = 'Log Items'

    def save(self, *args, **kwargs):
        # Sanity checks.
        if self.start_dt and self.end_dt:
            if self.end_dt < self.start_dt:
                raise ValidationError(
                    'End date-time cannot come before start date-time.')
        return super(LogItem, self).save(*args, **kwargs)
