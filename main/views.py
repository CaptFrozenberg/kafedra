from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import StepsListMixin

class MainPageView(TemplateView, StepsListMixin):
    template_name = 'mainpage.html'


