from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post


class Ex2view(TemplateView):
    template_name = "myapp/ex2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "this is just a demo post data"
        return context
