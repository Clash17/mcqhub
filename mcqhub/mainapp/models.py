from django.db import models


# Create your models here.
class Mcqdata(models.Model):
    question = models.CharField(max_length=1000)
    optiona = models.IntegerField(default=0)
    optionb = models.IntegerField(default=0)
    optionc = models.IntegerField(default=0)
    optiond = models.IntegerField(default=0)
    ans = models.IntegerField(default=0)

    def __str__(self):
        return self.question
