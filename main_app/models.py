from django.db import models

# Create your models here.
class Dog(models.Model):

    breed = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.breed

    class Meta:
        ordering = ['breed']