from django.conf import settings
from django.db import models

from posts.models import Post as BlogPost
# Create your models here.

class View(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    post = models.OneToOneField(BlogPost  , models.CASCADE)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.post , self.views_count)
    