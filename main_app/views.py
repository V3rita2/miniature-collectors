from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# models imports
from .models import Army

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class ArmiesList(TemplateView):
    template_name = "armies_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["armies"] = Army.objects.all()
        return context