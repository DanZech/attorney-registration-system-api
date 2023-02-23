from django.shortcuts import render
from rest_framework import viewsets
from .models import Attorney
from .serializers import AttorneySerializer

class AttorneyView(viewsets.ModelViewSet):
    queryset = Attorney.objects.all()
    serializer_class = AttorneySerializer
