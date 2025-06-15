from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

# Add the delete-all action to the router
router.register(r'delete-all', OrderViewSet, basename='order-delete-all')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/status/', OrderViewSet.as_view({'patch': 'update_status'}), name='order-status'),
    path('orders/all-details/', OrderViewSet.as_view({'get': 'all_details'}), name='order-all-details'),
] 