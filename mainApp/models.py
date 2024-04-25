from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    photo = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

class Talks(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    photo = models.FileField(null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.title