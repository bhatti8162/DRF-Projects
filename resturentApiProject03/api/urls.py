from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantViewSet,
    MenuItemViewSet,
    CustomerViewSet,
    OrderViewSet,
    TableViewSet,
)

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menu-items", MenuItemViewSet)
router.register("customers", CustomerViewSet)
router.register("orders", OrderViewSet)
router.register("tables", TableViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
