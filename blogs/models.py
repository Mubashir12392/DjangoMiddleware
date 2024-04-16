from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField(null=True)

    def __str__(self) -> str:
        return f'{self.title}'
    