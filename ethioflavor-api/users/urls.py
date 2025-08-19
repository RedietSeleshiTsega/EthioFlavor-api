from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.home), 
    path('register/', RegisterView.as_view(), name='register'),
]

