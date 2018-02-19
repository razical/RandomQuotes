from django.db import models

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    def __unicode__(self):
        return self.quote
