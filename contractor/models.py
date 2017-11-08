from django.db import models

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
