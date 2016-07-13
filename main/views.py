from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import SubjectListMixin, DocListMixin
from main.models import Document, Subject

SUPPORTED_EXTENSIONS = [
    'doc',
    'docx',
    'pdf',
    'pptx',
    'rar',
    'txt',
    'xls',
]

def compare(docs, ext):
    compared = []
    if docs:
        for doc in docs:
            extension = doc.file.name.split('.')[-1]
            if extension in ext:
                compared.append(('images/icons/{0}.png'.format(extension), doc))
            else:
                compared.append(('images/icons/no.png', doc))
    return compared


class MainPageView(TemplateView, SubjectListMixin):
    template_name = 'mainpage.html'

class SubjectView(TemplateView, SubjectListMixin):
    template_name = 'subject.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.show_masked = True
        else:
            self.show_masked = False
        return super(SubjectView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.subject_codename = self.kwargs['subject']
        context = super(SubjectView, self).get_context_data(**kwargs)
        subject = Subject.objects.get(code_name=self.subject_codename)
        context['subject_name'] = subject.name
        if self.show_masked:
            context['docs'] = compare(Document.objects.filter(subject__code_name=self.subject_codename),SUPPORTED_EXTENSIONS)
        else:
            context['docs'] = compare(Document.objects.filter(subject__code_name=self.subject_codename, masked=False),SUPPORTED_EXTENSIONS)
        return context

class InfoView(TemplateView, SubjectListMixin):
    def get_context_data(self, **kwargs):
        self.template_name = self.kwargs['title']
        context = super(InfoView, self).get_context_data(**kwargs)
        return context
