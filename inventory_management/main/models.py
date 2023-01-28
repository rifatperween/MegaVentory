from django.db import models

# Create your models here.
class warehouseItem(models.Model):
    name = models.CharField(max_length=40)
    value= models.IntegerField()
    hasShipped = models.BooleanField(default=False)
    def __str__(self):
        return self.name