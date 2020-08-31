from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiView.as_view()),
    path('<int:id>', views.ApiUpdateView.as_view()),
]