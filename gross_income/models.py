from django.db import models

# Create your models here.
class HighestMonthlyGrossIncome(models.Model):
    month = models.CharField(max_length=50,primary_key=True)
    highest_gross_income = models.DecimalField(max_digits=6,decimal_places=4)
