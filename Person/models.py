from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
def Length_CIN(value):
    if len(str(value))!=8:
        raise ValidationError("Your cin must have 8 integers!")
        # return "Your cin must have 8 integers!"
    return value
def Verif_email(value):
    if (str(value).endswith("@esprit.tn")==False):
        raise ValidationError("Your email {m} must ends with @esprit.tn",
                              params={'m':value})
    return value
class Person(AbstractUser):
    # cin=models.IntegerField(primary_key=True,validators=[MaxLengthValidator(8),MinLengthValidator(8)])
    cin=models.IntegerField(primary_key=True,validators=[Length_CIN])
    email=models.EmailField(unique=True)
    def __str__(self):
        return f"l'email de la personne est: {self.email}"
    class Meta:
        # verbose_name=('Personne')
        verbose_name_plural=('Personne')