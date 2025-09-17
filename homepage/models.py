from django.db import models

# Create your models here.


#leadership model
class Leadership(models.Model):
    leader_name = models.CharField(max_length=50)
    leader_position = models.CharField(max_length=50)
    leader_photo = models.ImageField(upload_to='leadership_photos/', blank=True, null=True)
    leader_caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.leader_name} - {self.leader_position}"
    


#projects model
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    project_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




