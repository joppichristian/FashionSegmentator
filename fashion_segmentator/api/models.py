from django.db import models
from django.utils import timezone

class ImageUploaded (models.Model):
    name = models.CharField(max_length=400)
    pic = models.ImageField(null=True,blank=True,upload_to=r"pics/")
    urls = models.CharField(null=True,blank=True,max_length=500)
    time = models.DateTimeField(editable=False)
    zip_result = models.BooleanField(default=False)
    heavy = models.BooleanField(default=False)

    # Methods
    def save(self, *args, **kwargs):
        # On save, update timestamps
        self.time = timezone.now()
        return super(ImageUploaded, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name + "; " + str(self.time))