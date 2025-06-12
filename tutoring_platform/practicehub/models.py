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
    
    
class UserQuizAttemptDetail(models.Model):
    """
    Stores the result for each individual question within a quiz attempt,
    linking the attempt to the specific question and whether it was answered correctly.
    """
    # Foreign key to the overall quiz attempt.
    attempt = models.ForeignKey(UserQuizAttempt, on_delete=models.CASCADE, related_name="details")

    # Foreign key to the question that was answered.
    # This now correctly links to your AquaRatTrain model.
    question = models.ForeignKey(AquaRatTrain, on_delete=models.CASCADE)

    # Boolean to track if the user's answer was correct.
    is_correct = models.BooleanField()

    class Meta:
        # Ensures that a question can only appear once per quiz attempt.
        # This mirrors the UNIQUE constraint in your SQL.
        unique_together = ('attempt', 'question')
        verbose_name = "User Quiz Attempt Detail"
        verbose_name_plural = "User Quiz Attempt Details"

    def __str__(self):
        return f"Question {self.question.id} in attempt {self.attempt.id} - {'Correct' if self.is_correct else 'Incorrect'}"