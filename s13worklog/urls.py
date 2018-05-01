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
        'categories',
        v.CategoriesView.as_view(),
        name='worklog.categories'
    ),
    path(
        'category/create',
        v.CategoryCreateView.as_view(),
        name='worklog.category.create'
    ),
    path(
        'category/delete/<int:pk>',
        v.CategoryDeleteView.as_view(),
        name='worklog.category.delete'
    ),
    path(
        'category/update/<int:pk>',
        v.CategoryUpdateView.as_view(),
        name='worklog.category.update'
    ),
    path(
        'tasks',
        v.TasksView.as_view(),
        name='worklog.tasks'
    ),
    path(
        'logitems',
        v.LogItemsView.as_view(),
        name='worklog.logitems'
    ),


    path(
        '',
        v.DashboardView.as_view(),
        name='worklog.dashboard'
    )
]
