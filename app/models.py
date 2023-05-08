from django.db import models



class offer(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    images = models.ImageField(upload_to='img')
    link = models.URLField(max_length=200, verbose_name='Link')
    review = models.IntegerField()
    def __str__(self):
        return self.title
    