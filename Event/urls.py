from django.urls import path
from . import views

urlpatterns = [
    path('bonjour/<str:classe>/', views.dynamic_interface, name='dynamic_interface'),
]