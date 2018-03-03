from django.db import models



class Subject(models.Model):

    title = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title



class LinkWrapper(models.Model):

    wraper_choice = [('PP', 'past papers'), ('PJ', 'practical journals'), ('NT', 'notes')]

    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    wraper = models.CharField(max_length=2, choices=wraper_choice, default='XX')

    def __str__(self):
        return self.title



class Link(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    link = models.URLField()
    linkwrapper = models.ForeignKey(LinkWrapper, on_delete=models.CASCADE)

    def __str__(self):
        return self.title