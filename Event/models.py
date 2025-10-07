from django.db import models
from Person.models import Person
from django.utils.timezone import datetime
# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)
    category_event=(
        ('M','Musique'),('S','Sport'),('C','Cinema')
    )
    category=models.CharField(max_length=255, choices=category_event)
    state=models.BooleanField(default=False)
    nbe_participant=models.IntegerField(default=0)
    evt_date=models.DateField("Date de l'evenement")
    creation_date=models.DateTimeField("Date Création",auto_now_add=True)
    updated_date=models.DateTimeField("Date màj",auto_now=True)
    organizer=models.ForeignKey(
        Person,
        # on_delete=models.CASCADE
        on_delete=models.SET_NULL,
        null=True,
    )
    participation=models.ManyToManyField(
        Person,
        related_name='participations'
    )
    class Meta:
        constraints=[models.CheckConstraint(
            check=models.Q(evt_date__gte=datetime.now()),
            name="Please check your event date!"
        )]
        ordering=('title','evt_date')
        verbose_name_plural=('Evenement')
class participation_event(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateField(auto_now=True)
    class Meta:
        unique_together=('person','event')