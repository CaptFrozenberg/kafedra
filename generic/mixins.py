from django.views.generic.base import ContextMixin
from main.models import Document, Subject

class SubjectListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(SubjectListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        context['kurses'] = [i for i in range(1, 5)]
        context['subjects_1_kurs'] = Subject.objects.filter(kurs=1, magistratura=False)
        context['subjects_2_kurs'] = Subject.objects.filter(kurs=2, magistratura=False)
        context['subjects_3_kurs'] = Subject.objects.filter(kurs=3, magistratura=False)
        context['subject_4_kurs'] = Subject.objects.filter(kurs=4, magistratura=False)
        context['subject_magistri'] = Subject.objects.filter(magistratura=True)
        return context

class DocListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(DocListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context