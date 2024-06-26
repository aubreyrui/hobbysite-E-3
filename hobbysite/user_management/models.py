from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length = 63)
	email_address = models.EmailField()

	def __str__ (self):
		return self.display_name
	
	def save(self, *args, **kwargs):
		# saving email address to the User database itself
		self.user.email = self.email_address
		self.user.save()
		super(Profile,self).save(*args,**kwargs)


# https://stackoverflow.com/questions/11488974/django-create-user-profile-on-user-creation
def create_user_profile(sender, instance, created, **kwargs): 
	if created:
		Profile.objects.create(user=instance, display_name=sender)

post_save.connect(create_user_profile, sender=User)