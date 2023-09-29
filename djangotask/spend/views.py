from django.db.models import Sum
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response

from .models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    revenue_sum = serializers.DecimalField(max_digits=9, decimal_places=2, read_only=True)
    spend_sum = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    impressions_sum = serializers.IntegerField(read_only=True)
    clicks_sum = serializers.IntegerField(read_only=True)
    conversion_sum = serializers.IntegerField(read_only=True)

    class Meta:
        model = SpendStatistic
        fields = ['date', 'name', 'spend_sum', 'impressions_sum', 'clicks_sum', 'conversion_sum', 'revenue_sum']


class SpendStatisticViewSet(viewsets.ModelViewSet):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticSerializer

    def list(self, request):
        queryset = (SpendStatistic.objects.values('date', 'name')
                    .annotate(
                    revenue_sum=Sum('revenue__revenue'),
                    spend_sum=Sum('spend'),
                    impressions_sum=Sum('impressions'),
                    clicks_sum=Sum('clicks'),
                    conversion_sum=Sum('conversion'),
                    ).order_by('date'))

        serializer = SpendStatisticSerializer(queryset, many=True)
        return Response(serializer.data)
