from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
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

    # def form_valid(self, form):
    #     # form.instance.user = self.request.user
    #     return super(ArmyCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('armies_detail', kwargs={'pk': self.object.pk})

    success_url = "/armies/"

class ArmyDetail(DetailView):
    model = Army
    template_name = "army_detail.html"

class ArmyUpdate(UpdateView):
    model = Army
    fields = ['name', 'image', 'desc']
    template_name = "army_update.html"
    success_url = '/armies/'

    def get_success_url(self):
        return reverse('army_detail', kwargs={'pk': self.object.pk})

class ArmyDelete(DeleteView):
    model = Army
    template_name = 'army_delete_confirm.html'
    success_url = "/armies/"