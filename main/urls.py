from django.conf.urls import patterns,url
from main.views import MainPageView, SubjectView, InfoView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^subject/(?P<subject>[a-zA-Z0-9-_]+)/$', SubjectView.as_view(), name='subject_name'),
    url(r'^info/(?P<title>[a-zA-Z0-9-_.]+)/$', InfoView.as_view(), name='info_view'),
]
