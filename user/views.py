
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserForm


class UserListView(generics.ListCreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class SignUp(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

