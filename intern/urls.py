from django.urls import path

from . import views

urlpatterns=[
        path("",views.intern,name="intern"),
        path("new/",views.newPage,name="newPage"),
]