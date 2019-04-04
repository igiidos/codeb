from django.db import models

# Create your models here.


class IndexMarkUp(models.Model):
    markup_title = models.CharField(max_length=255)
    markup_text = models.TextField(blank=True)