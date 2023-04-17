from django.db import models

class notes(models.Model):
    notes_title = models.CharField(max_length=250)
    notes = models.FileField(upload_to="notes/")

