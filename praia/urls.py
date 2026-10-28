from django.urls import path
from . import views

urlpatterns = [
    path("avaliar/", views.avaliar),
]
