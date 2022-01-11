from django.conf.urls import url
from crudapi import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^park$',views.parksApi),
    url(r'^park/([0-9]+)$',views.parksApi)
]