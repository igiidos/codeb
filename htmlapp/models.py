from django.db import models

# Create your models here.


class HtmlEditor(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

