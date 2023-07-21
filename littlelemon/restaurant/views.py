from django.shortcuts import render
from rest_framework import generics, viewsets

from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  
class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer


def index(request):
  return render(request, 'index.html', {})
