from django.db import models
from django.conf import settings 


class Photo(models.Model):
    file = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    
    def bucket_name(self):
        return settings.GS_BUCKET_NAME
        
    def file_name(self):
        return self.file.name
