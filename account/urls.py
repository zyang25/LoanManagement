from django.conf.urls import url
from account import views


urlpatterns = [
    # url(r'^detail/$', AccountView.as_view({
    #     "post":"registration",
    #     "post":"verify"
    #     }), name='account-detail'),

    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', views.verify, name='account-verify'),
]