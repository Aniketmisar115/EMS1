from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=10)
    year=models.CharField(max_length=10)
    mobile_num=models.CharField(max_length=500)

def _str_(self):
        return self.name