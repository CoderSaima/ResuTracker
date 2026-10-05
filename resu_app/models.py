from django.db import models
import os
from django.core.exceptions import ValidationError

def validate_pdf_extension(value):
    ext = os.path.splitext(value.name).lower
    if ext != '.pdf':
        raise ValidationError("Only authentic documents file can be proceed. e.g pdf file")


class ResuModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/',  validators=[validate_pdf_extension])
    transcript = models.FileField(upload_to='transcript/',  validators=[validate_pdf_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submitted by {self.name} at {self.uploaded_at}"