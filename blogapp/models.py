from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    excerpt = models.TextField(max_length=300, blank=True, null=True)  # Excerpt Field

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title