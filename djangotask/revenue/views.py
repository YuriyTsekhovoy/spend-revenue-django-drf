from django.db.models import Sum
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response

from .models import RevenueStatistic


class RevenueStatisticSerializer(serializers.ModelSerializer):
    revenue_sum = serializers.DecimalField(max_digits=9, decimal_places=2, read_only=True)
    spend_sum = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    impressions_sum = serializers.IntegerField(read_only=True)
    clicks_sum = serializers.IntegerField(read_only=True)
    conversion_sum = serializers.IntegerField(read_only=True)

    class Meta:
        model = RevenueStatistic
        fields = ['date', 'name', 'revenue_sum', 'spend_sum', 'impressions_sum',
                  'clicks_sum', 'conversion_sum']


class RevenueStatisticViewSet(viewsets.ModelViewSet):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializer

    def list(self, request):
        queryset = (RevenueStatistic.objects.values('date', 'name')
                    .annotate(
                    revenue_sum=Sum('revenue'),
                    spend_sum=Sum('spend__spend'),
                    impressions_sum=Sum('spend__impressions'),
                    clicks_sum=Sum('spend__clicks'),
                    conversion_sum=Sum('spend__conversion'),
                    ).order_by('date'))

        serializer = RevenueStatisticSerializer(queryset, many=True)
        return Response(serializer.data)
