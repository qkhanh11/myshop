from django.db import models

# Create your models here.
class VideoModel(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class OurteamModel(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(null=False,upload_to="about/")
    desc = models.CharField(max_length=30)
    fb = models.URLField(null=True)
    X = models.URLField(null=True)
    ig =models.URLField(null=True)
    ytb = models.URLField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class AboutModel(models.Model):
    head = models.CharField(max_length=100)
    desc = models.TextField()
    delete_flag = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.head