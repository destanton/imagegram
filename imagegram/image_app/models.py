from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Image(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=140)
    description = models.TextField()
    nsfw = models.BooleanField(blank=True, default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("created_time", )


class Profile(models.Model):
    user = models.OneToOneField('auth.User')

    def __str__(self):
        return self.user.username
