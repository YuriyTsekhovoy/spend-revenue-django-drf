from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = ('id', 'name', 'date', 'spend', 'impressions', 'clicks', 'conversion')

class SpendStatisticViewSet(viewsets.ModelViewSet):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticSerializer
