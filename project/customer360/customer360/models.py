from django.db import models
# Crea tus modelos aquí.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    social_media = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)


class Interaction(models.Model):
    CHANNEL_CHOICES = [
        ('phone', 'Teléfono'),
        ('sms', 'SMS'),
        ('email', 'Correo electrónico'),
        ('letter', 'Carta'),
        ('social_media', 'Redes Sociales'),
    ]

    DIRECTION_CHOICES = [
        ('inbound', 'Entrante'),
        ('outbound', 'Saliente'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()
    # social_media = models.CharField(max_length=100, blank=True)