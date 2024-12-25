from django.db import models

class Pinyin(models.Model):
    idiom = models.OneToOneField('Idiom', on_delete=models.CASCADE, related_name='pinyin')
    pinyin_text = models.CharField(max_length=20)  # Pinyin representation of the idiom
    tone_marks = models.CharField(max_length=20, blank=True, null=True)  # Optional tone marks

    def __str__(self):
        return self.pinyin_text


class Idiom(models.Model):
    text = models.CharField(max_length=4, unique=True)
    meaning = models.TextField(blank=True, null=True)  # Optional description
    example = models.TextField(blank=True, null=True)  # Example usage of the idiom
    derivation = models.TextField(blank=True, null=True)  # Origin or background of the idiom
    weight = models.IntegerField(default=1)  # Weight for ranking
    notes = models.TextField(blank=True, null=True)  # Additional notes

    def __str__(self):
        return self.text
