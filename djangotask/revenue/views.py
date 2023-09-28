from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import RevenueStatistic

class RevenueStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = ('id', 'name', 'spend', 'date', 'revenue')


class RevenueStatisticViewSet(viewsets.ModelViewSet):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializer

