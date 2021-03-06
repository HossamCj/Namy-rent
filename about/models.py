from django.db import models


class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goals = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')


class FAQ(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
