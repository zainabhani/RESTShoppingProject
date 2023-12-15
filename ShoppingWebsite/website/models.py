from django.db import models

# Create your models here.
class Products(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    price = models.FloatField()
    def __str__(self):
        return self.Name


