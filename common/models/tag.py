from django.db import models



class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=400)
  units = models.ManyToManyField('common.Unit')


class UnitTag(models.Model):
  id = models.AutoField(primary_key=True)
  unit = models.ForeignKey('common.Unit', on_delete=models.CASCADE)
  tag = models.ForeignKey('common.Tag', on_delete=models.CASCADE)