from django.db import models

# Create your models here.


class Achievement(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    points = models.IntegerField()
    image = models.ImageField(upload_to='achievement_images')

    def __unicode__(self):
        return self.name
