from django.http import HttpResponse
from django.shortcuts import render
from .tasks import some_task
from rest_framework import viewsets
from . import serialzers , models


class EmailCreatorViewSet(viewsets.ViewSet):
    serializer_class = serialzers.EmailCreatorSer
    queryset = models.EmailCreator.objects.all()

