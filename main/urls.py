from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from main.views import MainPageView, SubjectView, InfoView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    # url(r'^subject/(?P<subject>[a-zA-Z0-9-_]+)/$', login_required(SubjectView.as_view()), name='subject_name'),
    # если раскомментировать то незврегистрированный пользователь будет перенаправлен на форму входа
    url(r'^subject/(?P<subject>[a-zA-Z0-9-_]+)/$', SubjectView.as_view(), name='subject_name'),# закомментить если используется первый вариант
    url(r'^info/(?P<title>[a-zA-Z0-9-_.]+)/$', InfoView.as_view(), name='info_view'),
]
