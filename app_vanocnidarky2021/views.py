from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Prihlaseni(TemplateView):
    template_name = "prihlaseni.html"

class Index(TemplateView):
    template_name = "index.html"