from django.db import models


class Contact(models.Model):
    message = models.CharField(max_length=1000)
    email = models.EmailField(max_length=30)
    posted_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=17)

    def __str__(self):
        return self.name


# Create your models here.
