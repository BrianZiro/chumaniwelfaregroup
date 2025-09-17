from django.db import models

# Create your models here.
# aboutus/models.py
from django.db import models

class Leader(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    caption = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='leaders/', blank=True, null=True)

    class Meta:
        ordering = ['id']  # display in creation order

    def __str__(self):
        return f"{self.name} - {self.position}"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('community', 'Community'),
        ('financial', 'Financial Support'),
        ('social', 'Social Activities'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="projects/")
    link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
