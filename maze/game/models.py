from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)

	class Meta:
		ordering = ('-points',)
	
	def __str__(self):
		return str(self.user)

@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()