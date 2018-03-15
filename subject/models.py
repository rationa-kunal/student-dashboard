from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser





class Subject(models.Model):

    title = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title





class LinkWrapper(models.Model):

    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





class Tag(models.Model):

    choices = [('imp','imp'),
               ('practical program','practical program'),
               ('practical theory','practical theory'),
               ('by faculty','by faculty'),
               ('verified','verified'),
               ('cool','cool'),]
    title = models.CharField(max_length=50, choices=choices)

    def __str__(self):
        return self.title




class Link(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    link = models.URLField()
    linkwrapper = models.ForeignKey(LinkWrapper, on_delete=models.CASCADE)
    contributor = models.CharField(max_length=50, default="Anonymus")
    tag = models.ManyToManyField(Tag)

    class meta:
        default_permissions = ()

    def __str__(self):
        return self.title





class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)





class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

