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
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True, verbose_name='Profile photo')  #name of the directory
    # overrides label name that user sees
    @property
    def photo_url(self):  # created a property to make ti possbile to call object.photo_url in template or view
        if self.photo:
            return self.photo.url
        return "https://c2.staticflickr.com/4/3080/3162731295_1e33a2a077.jpg"


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
