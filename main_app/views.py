from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# models imports
from .models import Army

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class ArmiesList(TemplateView):
    template_name = "armies_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["armies"] = Army.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["armies"] = Army.objects.all()
            context["header"] = "Popular Armies"
        return context

class About(TemplateView):
    template_name = 'about.html'

class ArmyCreate(CreateView):
    model = Army
    fields = ['name', 'image', 'desc']
    template_name = "army_create.html"
    success_url = "/armies/"