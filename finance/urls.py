from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from finance import views

urlpatterns = [
    url(r'^schools/$', views.SchoolList.as_view(), name='school-list'),
    url(r'^schools/(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view(), name='school-detail'),
    url(r'^schools/(?P<pk>[0-9]+)/grants/$', views.SchoolGrantList.as_view(), name='school-grant-list'),
    url(r'^schools/(?P<pk>[0-9]+)/loans/$', views.SchoolLoanList.as_view(), name='school-loan-list'),
    url(r'^schools/(?P<pk>[0-9]+)/$', views.SchoolHighlight.as_view(), name='school-highlight'),

#Loans
    url(r'^loans/$', views.LoanList.as_view(), name='loan-list'),
    url(r'^loans/(?P<pk>[0-9]+)/$', views.LoanDetail.as_view(), name='loan-detail'),
    url(r'^loans/(?P<pk>[0-9]+)/$', views.LoanHighlight.as_view(), name='loan-highlight'),

#Grants
    url(r'^grants/$', views.GrantList.as_view(), name='grant-list'),
    url(r'^grants/(?P<pk>[0-9]+)/$', views.GrantDetail.as_view(), name='grant-detail'),
    url(r'^grants/(?P<pk>[0-9]+)/$', views.GrantHighlight.as_view(), name='grant-highlight'),

    url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
