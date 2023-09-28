from django.urls import path

from .views import SpendStatisticViewSet

urlpatterns = [
    path('spend-statistics/', SpendStatisticViewSet.as_view({'get': 'list', 'post': 'create'}), name='spend-statistics'),
    path('spend-statistics/<int:pk>/', SpendStatisticViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='spend-statistic-detail'),
]
