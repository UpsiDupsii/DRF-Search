from django.db import models

# Create your models here.
class Empl_Details(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name