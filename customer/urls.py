from django.conf.urls import url
from customer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^list/$', views.ListCustomer.as_view(), name='customer-list'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.CustomerDetail.as_view(), name='customer-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)