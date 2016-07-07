from django.conf.urls import patterns,url
from main.views import MainPageView, SubjectView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^(?P<subject>[a-zA-Z0-9-]+)/$', SubjectView.as_view(), name='subject')
]
