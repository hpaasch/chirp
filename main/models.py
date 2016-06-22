from django.db import models
from django.db.models.signals import post_save  # very commonly used
from django.dispatch import receiver  # goes with post_save and other signals


class Chirp(models.Model):
    body = models.CharField(max_length=141)
    created = models.DateTimeField(auto_now_add=True)
    bird = models.ForeignKey("auth.User")  # avoids import of the other method (User)

    class Meta:
        ordering = ['-created']  # descending order


class StopWord(models.Model):  # adding this so a non expert can manage the list
    word = models.CharField(max_length=26)


class Profile(models.Model):
    user = models.OneToOneField('auth.user')  # this ties to the Django table and expands
    favorite_bird = models.CharField(max_length=100, null=True)


@receiver(post_save, sender=StopWord)  # post_save is the signal i want to subscribe to
def say_hello(**kwargs):
    print('hello world')  # can see in terminal


@receiver(post_save, sender='auth.User')  # ties it to the User
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')  # you can see in Terminal that this user Object shows
    # print(kwargs)  # can see in terminal

    if created:
        Profile.objects.create(user=instance)  # this hooks up profile to user
