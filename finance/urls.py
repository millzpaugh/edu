from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from finance import views

urlpatterns = [
    url(r'^schools/$', views.SchoolList.as_view(), name='school-list'),
    url(r'^schools/(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view(), name='school-detail'),
    url(r'^schools/(?P<pk>[0-9]+)/grants/$', views.SchoolGrantList.as_view()),
    url(r'^schools/(?P<pk>[0-9]+)/loans/$', views.SchoolLoanList.as_view(), name='loan-list'),
    url(r'^schools/(?P<pk>[0-9]+)/highlight/$', views.SchoolHighlight.as_view(), name='school-highlight'),

    url(r'^$', views.api_root),

    # url(r'^(?P<year>[0-9]+)/loans/$', views.LoanListByYear.as_view()),
    # url(r'^(?P<year>[0-9]+)/grants/$', views.GrantListByYear.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
