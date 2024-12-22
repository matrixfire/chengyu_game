from django.db import models

class Idiom(models.Model):
    text = models.CharField(max_length=4, unique=True)
    meaning = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.text
