from django.db import models

# Create your models here.
class HeroModel(models.Model):
    name = models.CharField(max_length=15)
    text = models.TextField()
    img = models.ImageField(null=False,upload_to="hero/")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name