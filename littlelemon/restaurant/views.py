from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu


# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated]
  
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  
class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer


def index(request):
  return render(request, 'index.html', {})
