from django.db import models


class Chirp(models.Model):
    body = models.CharField(max_length=141)
    created = models.DateTimeField(auto_now_add=True)
    bird = models.ForeignKey("auth.User")  # avoids import of the other method (User)

    class Meta:
        ordering = ['-created']  # descending order
