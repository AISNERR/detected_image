from django.db import models
 


class Image(models.Model):
    title = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", null=True)