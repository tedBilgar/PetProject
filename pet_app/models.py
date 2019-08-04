from django.db import models

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=50, null=False)
    home = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.home)