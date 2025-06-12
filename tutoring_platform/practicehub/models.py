from django.db import models
from django.contrib.auth.models import User

class UserQuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Quiz Attempt on {self.timestamp.strftime('%Y-%m-%d')}"

class AquaRatTrain(models.Model):
    question = models.TextField(null=False)
    options = models.JSONField(null=False)
    rationale = models.TextField(null=True, blank=True)
    correct = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        db_table = 'aqua_rat_train'
        
    def __str__(self):
        return f"Question {self.id}: {self.question[:50]}..."