from django.db import models

# Create your models here.
class QuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True, help_text="Optional explanation or answer.")

    def __str__(self):
        return self.question[:50]
