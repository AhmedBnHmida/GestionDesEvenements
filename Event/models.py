from django.db import models
from Person.models import Person
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Musique', 'Musique'),
        ('Cinema', 'Cinéma'),
        ('Sport', 'Sport'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    state = models.BooleanField(default=False)
    nbe_participant = models.IntegerField(default=0)
    evt_date = models.DateField("Date de l'événement")
    creation_date = models.DateTimeField("Date Création", auto_now_add=True)
    updated_date = models.DateTimeField("Date MAJ", auto_now=True)
    organizer = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        related_name='organized_events'
    )
    
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(evt_date__gte=now()),
                name="check_event_date"
            )
        ]
        ordering = ('title', 'evt_date')
        verbose_name_plural = 'Événements'
    
    def __str__(self):
        return f"{self.title} - {self.get_category_display()} - {self.evt_date}"

class Participation(models.Model):
    person = models.ForeignKey(
        Person, 
        on_delete=models.CASCADE,
        related_name='event_participations'
    )
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE,
        related_name='event_participations'
    )
    participation_date = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = ('person', 'event')
        verbose_name_plural = 'Participations'
    
    def __str__(self):
        return f"{self.person} - {self.event.title}"