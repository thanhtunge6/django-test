from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^testapp/', views.MyView.as_view(), name='testapp'),
]