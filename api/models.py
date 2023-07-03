from django.db import models
import os, random, math
from django.conf import settings
from datetime import datetime ,date, timedelta

# Create your models here.


def save_profile_image(instance, filename):
        file_extension = os.path.splitext(filename)[1].lstrip('.')
        random_number = random.randint(0, 99)
        current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')+str(random_number)+str(random_number)
        target_dir = f'media_folder'
        file_dir = os.path.join(settings.MEDIA_ROOT, target_dir)
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir, 0o777)
        return os.path.join(target_dir, f'{current_datetime}.{file_extension}')


class Media(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    profile_pic = models.FileField(max_length=256, upload_to = save_profile_image, null=True, blank=True)
