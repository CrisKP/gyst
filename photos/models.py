from django.db import models


class Photo(models.Model):
    file = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
