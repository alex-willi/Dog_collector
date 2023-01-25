from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse


# Create your views here.

class Dog:
    def __init__(self, breed, image):
        self.breed = breed
        self.image = image

dogs = [
    Dog("Golden Retriever", "https://imgur.com/4qmmRFj.jpg"),
    Dog("German Shepherd", "https://imgur.com/yyZwINK.jpg"),
    Dog("Poodle", "https://imgur.com/mpR1cot.jpg"),
    Dog("Bulldog", "https://imgur.com/2uHl578.jpg"),
    Dog("Beagle", "https://imgur.com/JsdylJO.jpg"),
    Dog("Labrador Retriever", "https://imgur.com/GVmp0Gz.jpg"),
]


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class DogList(TemplateView):
    template_name = "dog_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dogs'] = dogs
        return context