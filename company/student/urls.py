from django.urls import path
from . import views
urlpatterns=[path('l/',views.myfun),
             path('k/',views.myfun2,name="myfun2"),
             path('',views.read,name="read"),
             path('delete/<int:id>',views.delete,name="delete"),
             path('edit/<int:id>',views.edit,name="edit"),

            ]