from re import template
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='myapp/index.html')),
    path('ex2', views.Ex2view.as_view())
]
