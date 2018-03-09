from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):

    title = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title



class LinkWrapper(models.Model):

    wrapper_choice = [('PP', 'past papers'), ('PJ', 'practical journals'), ('NT', 'notes')]

    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    wrapper = models.CharField(max_length=2, choices=wrapper_choice, default='XX')

    def __str__(self):
        return self.title



class Link(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    link = models.URLField()
    linkwrapper = models.ForeignKey(LinkWrapper, on_delete=models.CASCADE)
    contributor = models.CharField(max_length=50, default="Anonymus")

    class meta:
        default_permissions = ()

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)



class Dislike(models.Model):
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)

