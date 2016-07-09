from django.views.generic.base import ContextMixin
from main.models import Document

class StepsListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(StepsListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context

class DocListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(DocListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context