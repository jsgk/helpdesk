from django.db import models
from helpdesk.users.models import User

class Status(models.Model):
    beschreibung = models.CharField(max_length = 20)

class Bearbeiter(User):
    pass
    
class Defekt(models.Model):
    raum=models.CharField(max_length=20)
    geraet=models.CharField(max_length=20)
    fehler=models.CharField(max_length=100)
    uhrzeit=models.DateTimeField(auto_now_add=True,auto_now=False)
    status=models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)
    bearbeiter=models.ForeignKey(Bearbeiter, models.SET_NULL, blank=True, null=True, related_name='bearbeiter')
    melder=models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
