from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.name,self.message)
