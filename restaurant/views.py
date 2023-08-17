from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated


class MenuItemsView(generics.ListCreateAPIView):
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


# def index(request):
#     return render(request, 'index.html', {})


