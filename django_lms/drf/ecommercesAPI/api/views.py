from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [permission.isAuthentication]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # permission_classes = [permission.isAuthentication]
