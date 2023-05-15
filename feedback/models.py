from django.db import models


class Feedback(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.CharField(max_length=500)
