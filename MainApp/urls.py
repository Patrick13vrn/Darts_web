from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='MainApp'),
    path('contact/', views.contact, name='contact'),
]
