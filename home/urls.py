from django.conf.urls import url,include
from django.contrib import admin
from home import views
urlpatterns = [
    url(r'^index/',views.index ),
    url(r'^login/',views.login ),
]