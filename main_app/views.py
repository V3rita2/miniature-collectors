from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

# class Armies(TemplateView):
#     template_name = 'armies.html'

class Army: 
    def __init__(self, name, image, desc):
        self.name = name
        self.image = image
        self.desc = desc

armies = [
    Army("Imperial Guard", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2F06%2Fe3%2Fc6%2F06e3c6ade811a208913ebfb8827ffe3d.jpg&f=1&nofb=1", 
            "The guard are the backbone of the Imperium, fielding massive artillery batteries, a formidable front line of infantry troops, backed up by mechanized tanks and walkers."),
    Army("Necrons", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.MFJAY7jVElYGowjuZqpQaAHaEK%26pid%3DApi&f=1", 
            "The Necrons are an ancient race, who gave up their biological forms for immortality in a war with the gods. Newly awakened from their tombs, they employ terrifyingly powerful gauss weaponry to re-conquer the stars")
]

class ArmiesList(TemplateView):
    template_name = "armies_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["armies"] = armies
        return context