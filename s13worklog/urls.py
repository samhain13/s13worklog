from django.urls import path

from . import views as v


urlpatterns = [
    path(
        'testing/dev-test-view',
        v.DevTestView.as_view(),
        name='dev-test-view'
    ),
]
