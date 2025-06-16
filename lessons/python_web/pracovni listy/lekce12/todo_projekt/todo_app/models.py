from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    # pridani reference k uzivateli
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # old code 
    text = models.CharField(max_length=200, verbose_name="Úkol")
    poznamka = models.TextField(blank=True, verbose_name="Poznámka")
    ocekavane = models.DateField(null=True, blank=True, verbose_name="Očekávaný termín")
    predmet = models.CharField(max_length=100, blank=True, verbose_name="Předmět")
    done = models.BooleanField(default=False, verbose_name="Splněno")
    created = models.DateTimeField(default=timezone.now, verbose_name="Vytvořeno")
    completed = models.DateTimeField(null=True, blank=True, verbose_name="Dokončeno")
    deleted = models.BooleanField(default=False, verbose_name="Smazáno")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Smazáno v")
    
    def __str__(self):
        return self.text