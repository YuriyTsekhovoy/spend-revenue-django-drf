from django.urls import path

from .views import RevenueStatisticViewSet

urlpatterns = [
    path('revenue-statistics/', RevenueStatisticViewSet.as_view({'get': 'list', 'post': 'create'}), name='revenue-statistics'),
    path('revenue-statistics/<int:pk>/', RevenueStatisticViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='revenue-statistic-detail'),
]
