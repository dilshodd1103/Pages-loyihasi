from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class SettingPageView(TemplateView):
    template_name = 'setting.html'

class CommonPageView(TemplateView):
    template_name = 'common.html'