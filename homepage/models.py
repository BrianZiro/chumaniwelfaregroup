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



