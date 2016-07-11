from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import SubjectListMixin, DocListMixin
from main.models import Document, Subject

class MainPageView(TemplateView, SubjectListMixin):
    template_name = 'mainpage.html'

class SubjectView(TemplateView, SubjectListMixin):
    template_name = 'subject.html'

    def get_queryset(self):
        self.subject_name = self.request.GET['name']
        queryset = super(SubjectView, self).get_queryset()
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            self.subject = self.kwargs['subject']
        except:
            pass
        return super(SubjectView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        #self.subject_codename = self.request.path.split('/')[-1]
        self.subject_codename = self.kwargs['subject']
        context = super(SubjectView, self).get_context_data(**kwargs)
        subject = Subject.objects.get(code_name=self.subject_codename)
        context['subject_name'] = subject.name
        context['docs'] = Document.objects.filter(subject__name=self.subject_codename)

        return context
