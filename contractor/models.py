from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class work(models.Model):
    workName = models.CharField(max_length=300)
    workPic = models.CharField(max_length=1000)

    def __str__(self):
        return self.workName


class worker(models.Model):
    work = models.ForeignKey(work, on_delete=models.CASCADE)
    workerName = models.CharField(max_length=500)
    workerPic = models.CharField(max_length=1000, null=True)
    aboutWorker = models.CharField(max_length=2000)
    hourlyRate = models.CharField(max_length=100)

    def __str__(self):
        return self.workerName

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    workCategory = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=20, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    pricePerHour = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

def create_profile (sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)