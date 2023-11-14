from django.db import models

# Create your models here.
class todoCreate(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    address = models.TextField()
    date = models.DateTimeField()


    class Meta:
        def __str__(self) -> str:
            return self.name
        
        