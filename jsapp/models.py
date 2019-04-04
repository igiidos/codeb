from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Name(models.Model):
    text_code = models.TextField()
    pub_date = models.DateTimeField(auto_now=False)
    mod_date = models.DateTimeField(auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=50)

    def __str__(self):
        return self.author
