from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from finance import views

urlpatterns = [
    url(r'^schools/$', views.SchoolList.as_view()),
    url(r'^schools/(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)