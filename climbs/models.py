from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    is_climbed = models.BooleanField()
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Step(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='steps', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField()
    is_missed = models.BooleanField()
    date = models.DateTimeField()
