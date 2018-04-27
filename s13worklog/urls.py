from django.urls import path

from . import views as v


urlpatterns = [
    path(
        'testing/dev-test-view',
        v.DevTestView.as_view(),
        name='dev-test-view'
    ),
    path(
        'login',
        v.LoginView.as_view(),
        name='worklog.login'
    ),
    path(
        'logout',
        v.LogoutView.as_view(),
        name='worklog.logout'
    ),
    path(
        '',
        v.DashboardView.as_view(),
        name='worklog.dashboard'
    )
]
