from django.db import models

class RetailData(models.Model):
    SEGMENT_CHOICES = [
        ('first_party', 'First Party'),
        ('third_party', 'Third Party'),
    ]
    
    # Original file fields
    merchant = models.TextField()
    sku = models.TextField()
    country = models.CharField(max_length = 3)  # ISO code
    
    # Annotation fields
    retailer = models.TextField(blank = True, null = True)
    segment = models.CharField(max_length = 20, choices = SEGMENT_CHOICES, blank = True, null = True)
    
    class Meta:
        unique_together = ['merchant', 'sku', 'country']
    
    def __str__(self):
        return f"{self.merchant} - {self.sku} - {self.country}"