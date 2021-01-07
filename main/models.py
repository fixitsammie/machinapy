from django.db import models
from authapp.models import User
PARTICIPANT_TYPES = [
    ('Band', 'Band'),
    ('Carriage', 'Carriage')

]


class Recruit(models.Model):
    name = models.CharField(max_length=100)
    manager_email = models.EmailField(max_length=100)
    foundation_date = models.DateField(blank=True)
    participant_type = models.CharField(max_length=10, choices=PARTICIPANT_TYPES)
    order_id =  models.IntegerField(null=True,blank=True)

