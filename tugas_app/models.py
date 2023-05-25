from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    deadline = models.DateField()

    def __str__(self):
        return self.title
