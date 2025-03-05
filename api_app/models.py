from django.db import models

# Create your models here.


class Student(models.Model):
    names = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    adm_no = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.names