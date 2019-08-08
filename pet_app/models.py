from django.db import models

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=50, null=False)
    home = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.home)


class Owner(models.Model):
    cat = models.ForeignKey(Cat, related_name='onwers_of_cat', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    money = models.IntegerField()
    occupation = models.CharField(max_length=100, null=False)

    class Meta:
        unique_together = ['cat', 'name']
        ordering = ['name']

    def __str__(self):
        return '%d: %s' % (self.money, self.name)
