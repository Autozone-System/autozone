from django.db import models



class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=400)
  vehicles = models.ManyToManyField('common.Vehicle')


class VehicleTag(models.Model):
  id = models.AutoField(primary_key=True)
  vehicle = models.ForeignKey('common.Vehicle', on_delete=models.CASCADE)
  tag = models.ForeignKey('common.Tag', on_delete=models.CASCADE)