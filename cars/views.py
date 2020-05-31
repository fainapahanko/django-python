from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from cars.permissions import IsOwnerOrReadOnly
from cars.models import Car


# Create your views here.
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = (IsAuthenticated, )


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )


class CarDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

