from django.db.models import EmailField
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

from utils.get_photo_path import get_photo_path
from users.user_manager import UserManager


class User(AbstractUser):
	email = EmailField(blank=False, db_index=True, unique=True)
	image = ResizedImageField(
		null=True, blank=True,
		size=[200, 200],
		quality=100,
		upload_to=get_photo_path
	)
 
	objects = UserManager()
 
	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = []
 
	def __str__(self):
		return f"{self.first_name} {self.last_name}"
 