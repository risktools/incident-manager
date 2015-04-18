from django.db import models

# Create your models here.


from django.db import models

class Incident(models.Model):
  identifier = models.CharField(max_length=10, unique=True)
  name       = models.CharField(max_length=100)
  level      = models.IntegerField(default=5)
  date       = models.DateField()
  incident_group = models.CharField(max_length=200)
  state       = models.CharField(max_length=50)
  owner       = models.CharField(max_length=50)

  def __unicode__(self):
    return "%s %s %s %s %s %s %s" % (self.identifier, self.name, self.date, self.incident_group, self.level, self.state, self.owner)
