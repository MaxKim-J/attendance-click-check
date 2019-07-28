from django.db import models

# Create your models here.


class Status(models.Model):
    attend_name = models.CharField(max_length=100)
    status_time = models.DateTimeField("Status Time")

    def __str__(self):
        return self.attend_name


class Comers(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Join Time")

    def __str__(self):
        return self.user_name