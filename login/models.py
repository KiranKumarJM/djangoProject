from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #mobile_no = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"