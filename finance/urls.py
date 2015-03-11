from django.conf.urls import url
from finance.views import school_detail, school_list

urlpatterns = [
    url(r'^schools/$', school_list),
    url(r'^schools/(?P<pk>[0-9]+)/$', school_detail),
]