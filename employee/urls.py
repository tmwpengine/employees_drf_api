from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^employees/$', views.employee_list),
    url(r'^employees/(?P<pk>[0-9]+)/$', views.employee_detail),
    url(r'^companies/$', views.CompanyList.as_view()),
    url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),
]
