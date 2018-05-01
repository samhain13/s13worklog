from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from .forms import CategoryForm
from .forms import LoginForm
from .forms import LogItemForm
from .forms import TaskForm
from .models import Category
from .models import LogItem
from .models import Task


class UIContextMixin:
    ui_title = 'UI Title'
    ui_description = 'UI Description'
    template_name = '_base.html'

    def get_context_data(self, **kwargs):
        context = super(UIContextMixin, self).get_context_data(**kwargs)
        for prop in [x for x in dir(self) if x.startswith('ui_')]:
            context[prop] = getattr(self, prop)
        return context


class WorkLogMixin(UIContextMixin, LoginRequiredMixin):
    login_url = reverse_lazy('worklog.login')

    def form_valid(self, form):
        messages.success(
            self.request,
            getattr(self, 'success_message', 'Operation successful.')
        )
        return super(WorkLogMixin, self).form_valid(form)

    def form_invalid(self, form):
        for key, message in form.errors.items():
            messages.error(self.request, message[0])
        return super(WorkLogMixin, self).form_invalid(form)


class WorkLogDeleteMixin(WorkLogMixin, DeleteView):

    def get(self, request, *args, **kwargs):
        messages.warning(
            self.request,
            'Are you sure you want to delete this item?'
        )
        return super(WorkLogDeleteMixin, self).get(
            self.request, *self.args, **self.kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(
            self.request,
            getattr(self, 'success_message', 'Operation successful.')
        )
        return super(WorkLogDeleteMixin, self).post(
            self.request, *self.args, **self.kwargs)


class LoginView(UIContextMixin, FormView):
    form_class = LoginForm
    success_url = reverse_lazy('worklog.dashboard')
    ui_title = 'Log In'
    ui_description = 'Please log in to continue.'

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(self.request, user)
            messages.success(
                self.request, 'Welcome back, {}!'.format(user.username))
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class LogoutView(WorkLogMixin, TemplateView):
    template_name = '_base.html'

    def get(self, request, *args, **kwargs):
        logout(self.request)
        messages.success(self.request, 'Thank you for using S13WorkLog.')
        return redirect(reverse_lazy('worklog.login'))


class DashboardView(WorkLogMixin, TemplateView):
    template_name = 'dashboard.html'
    ui_description = 'S13WorkLog account overview.'
    ui_title = 'Dashboard'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['latest_categories'] = \
            Category.objects.all().order_by('-pk')[:5]
        context['latest_tasks'] = \
            Task.objects.all().order_by('-pk')[:10]
        context['latest_logitems'] = \
            LogItem.objects.all().order_by('-pk')[:25]
        return context


class CategoriesView(WorkLogMixin, ListView):
    model = Category
    template_name = 'list-generic.html'
    ui_action_create = 'worklog.category.create'
    ui_action_delete = 'worklog.category.delete'
    ui_action_update = 'worklog.category.update'
    ui_description = 'A listing of available task categories.'
    ui_title = 'Task Categories'


class CategoryCreateView(WorkLogMixin, CreateView):
    form_class = CategoryForm
    model = Category
    success_message = 'Category added.'
    success_url = reverse_lazy('worklog.categories')
    template_name = 'form-generic.html'
    ui_button_text = 'Create Category'
    ui_description = 'A form for creating a task category.'
    ui_objtype = 'category'
    ui_title = 'Create a Category'


class CategoryDeleteView(WorkLogDeleteMixin):
    form_class = CategoryForm
    model = Category
    success_message = 'Category deleted.'
    success_url = reverse_lazy('worklog.categories')
    template_name = 'form-generic.html'
    ui_button_text = 'Delete Category'
    ui_description = 'A form for deleting a task category.'
    ui_objtype = 'category'
    ui_title = 'Delete a Category'


class CategoryUpdateView(WorkLogMixin, UpdateView):
    form_class = CategoryForm
    model = Category
    success_message = 'Category updated.'
    success_url = reverse_lazy('worklog.categories')
    template_name = 'form-generic.html'
    ui_button_text = 'Update Category'
    ui_description = 'A form for updating a task category.'
    ui_objtype = 'category'
    ui_title = 'Update a Category'


class TasksView(WorkLogMixin, ListView):
    model = Task
    template_name = 'list-generic.html'
    ui_description = 'A listing of available tasks.'
    ui_title= 'Tasks'


class TaskCreateView(WorkLogMixin, CreateView):
    form_class = TaskForm
    model = Task
    template_name = 'form-generic.html'


class LogItemsView(WorkLogMixin, ListView):
    model = LogItem
    template_name = 'list-generic.html'
    ui_description = 'A listing of available work logs.'
    ui_title = 'Work Logs'


# ------------- For testing only.

class DevTestView(TemplateView):
    '''A view that simply tests whether Jinja2 is working.'''

    template_name = 'devtestview.html'

    def get_context_data(self, **kwargs):
        context = super(DevTestView, self).get_context_data(**kwargs)
        context['ui_title'] = 'Dev Test View'
        return context
