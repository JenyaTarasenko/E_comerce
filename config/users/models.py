from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Профиль Usera"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_pofile_images')
    contact_number = models.CharField(max_length=50, default="+3809912345")

    def __str__(self):
        return self.user.username#переходим в username(.user вызовет ошибку)

