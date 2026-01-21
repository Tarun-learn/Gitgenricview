from django.shortcuts import render
from .models import *
from .serializer import *
# from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework.viewsets import GenericViewSet


# class StudentClass(GenericViewSet,
#                    ListModelMixin,
#                    CreateModelMixin,
#                    ):

#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerilaier


#genric viewset
class StudentGenricClass(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerilaier

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    