from django.db import models
from spend import models as spend

# Create your models here.
class RevenueStatistic(models.Model):
   name = models.CharField(max_length=255)
   spend = models.ForeignKey('spend.SpendStatistic', on_delete=models.SET_NULL, null=True,
                             related_name='revenue')
   date = models.DateField()
   revenue = models.DecimalField(max_digits=9, decimal_places=2,   default=0)
