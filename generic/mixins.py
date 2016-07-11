from django.views.generic.base import ContextMixin
from main.models import Document, Subject

class SubjectListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(SubjectListMixin, self).get_context_data(**kwargs)
        context['current_url'] = self.request.path
        context['subject_pack'] = [Subject.objects.filter(kurs=i, magistratura=False) for i in range(1, 5)]
        context['subjects_magistratura'] = Subject.objects.filter(magistratura=True)
        return context

class DocListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(DocListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context