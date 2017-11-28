from django.shortcuts import render
from django.views.generic import TemplateView


class Discus(TemplateView):
    template_name = "mederoblog/dicuss.html"
