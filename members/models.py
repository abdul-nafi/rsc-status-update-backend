from django.contrib.auth.models import AbstractUser
from django.db import models

class PartyUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class PartyMember(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True)
    is_working = models.BooleanField(default=False)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    is_exited_country = models.BooleanField(default=False)
    is_on_vacation = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'contact_number')

    def __str__(self):
        return f"{self.name} ({self.contact_number})"
