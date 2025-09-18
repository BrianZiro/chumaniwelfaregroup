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
    
#events model
class Event(models.Model):
    title = models.CharField(max_length=200)  # Event title
    description = models.TextField()          # Event details
    image = models.ImageField(
        upload_to="events/", 
        blank=True, 
        null=True,
        help_text="Upload event poster or image"
    )
    start_date = models.DateTimeField()       # Event start
    end_date = models.DateTimeField(blank=True, null=True)  # Event end (optional)

    created_at = models.DateTimeField(auto_now_add=True)  # When added
    updated_at = models.DateTimeField(auto_now=True)      # Last update

    def __str__(self):
        return self.title



class Resource(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('damaged', 'Damaged'),
        ('planned', 'Planned'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='resources/', blank=True, null=True)

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return f"{self.name} ({self.quantity})"



