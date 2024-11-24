from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

from task.models import Task

from task.serializer import TaskSerializer,SignUpSerializer

from rest_framework import authentication,permissions

# Create your views here.


class Signupview(CreateAPIView):

    serializer_class=SignUpSerializer


class TasklistcreateView(ListCreateAPIView):

    serializer_class=TaskSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    queryset=Task.objects.all()

    def perform_create(self,serializer):

        serializer.save(owner=self.request.user)


class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):


    serializer_class=TaskSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    queryset=Task.objects.all()

