from django.http import HttpResponse
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model


def home(request):
    return HttpResponse("Welcome to EthioFlavor API 👋")

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
