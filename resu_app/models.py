from django.db import models

class ResuModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    transcript = models.FileField(upload_to='transcript/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submitted by {self.name} at {self.uploaded_at}"