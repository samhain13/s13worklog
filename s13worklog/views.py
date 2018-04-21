from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import TemplateView

from .forms import LoginForm


class WorkLogMixin(LoginRequiredMixin):
    login_url = reverse_lazy('worklog.login')


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('worklog.dashboard')
    template_name = 'devtestview.html'  # Change this later.

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


class DashboardView(WorkLogMixin, TemplateView):
    template_name = 'devtestview.html'  # Change this later.


# ------------- For testing only.

class DevTestView(TemplateView):
    '''A view that simply tests whether Jinja2 is working.'''

    template_name = 'devtestview.html'

    def get_context_data(self, **kwargs):
        context = super(DevTestView, self).get_context_data(**kwargs)
        context['title'] = 'Dev Test View'
        return context
