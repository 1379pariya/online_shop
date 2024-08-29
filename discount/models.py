from django.db import models
from django.conf import settings


# مدل تخفیف
class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # درصد تخفیف
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def is_valid(self):
        from django.utils import timezone
        return self.valid_from <= timezone.now() <= self.valid_to

    def __str__(self):
        return f"Discount Code: {self.code} - {self.percentage}%"
