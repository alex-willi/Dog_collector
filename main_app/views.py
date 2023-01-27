from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse

# import models
from .models import Dog


# Create your views here.

# class Dog:
#     def __init__(self, breed, image):
#         self.breed = breed
#         self.image = image

# dogs = [
#     Dog("Golden Retriever", "https://imgur.com/4qmmRFj.jpg"),
#     Dog("German Shepherd", "https://imgur.com/yyZwINK.jpg"),
#     Dog("Poodle", "https://imgur.com/mpR1cot.jpg"),
#     Dog("Bulldog", "https://imgur.com/2uHl578.jpg"),
#     Dog("Beagle", "https://imgur.com/JsdylJO.jpg"),
#     Dog("Labrador Retriever", "https://imgur.com/GVmp0Gz.jpg"),
# ]


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class DogList(TemplateView):
    template_name = "dog_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("breed")
        if name != None:
            context["dogs"] = Dog.objects.filter(breed__icontains=name)
            context["header"] = f"searching for {name}"
        else:
            context['dogs'] = Dog.objects.all()
            context['header'] = "Dog Collector"
        return context

class DogCreate(CreateView):
    model = Dog
    fields = ['breed', 'img']
    template_name = "dogs_create.html"
    success_url = "/dogs/"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})


class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'img']
    template_name = "dog_update.html"
    success_url = "/dogs/"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

class DogDelete(DeleteView):
    model = Dog
    template_name = "dog_delete.html"
    success_url = "/dogs/"