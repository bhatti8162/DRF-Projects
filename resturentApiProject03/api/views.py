from rest_framework.viewsets import ModelViewSet
from .models import Restaurant, MenuItem, Customer, Order, Table
from .serializers import (
    RestaurantSerializer,
    MenuItemSerializer,
    CustomerSerializer,
    OrderSerializer,
    TableSerializer,
)

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
