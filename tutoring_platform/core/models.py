from django.db import models

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='tutors/')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author}: {self.quote[:50]}..."