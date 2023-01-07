from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
