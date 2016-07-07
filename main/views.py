from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import StepsListMixin, DocListMixin
from main.models import Document

class MainPageView(TemplateView, StepsListMixin):
    template_name = 'mainpage.html'

class SubjectView(TemplateView, DocListMixin):
    template = 'subject.html'
    def get(self, request, *args, **kwargs):
        try:
           self.subject = self.request.GET['subject']
        except:
            pass
    def get_context_data(self, **kwargs):
        context = super(SubjectView, self).get_context_data(**kwargs)
        context['docs'] = Document.objects.filter(subject=self.subject)
        return context