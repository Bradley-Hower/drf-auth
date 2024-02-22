from django.db import models
from django.contrib.auth import get_user_model

class Lamp(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  description = models.TextField()
  class Lights(models.TextChoices):
    LED = "LED", "Light Emitting Diode"
    ICL = "ICL", "Incandescent"
    Neon = "Neon", "Neon"
    HL = "HL", "Halogen"
    CFL = "CFL", "Compact Fluorescent Lighting"
  light_type = models.CharField(max_length=64, choices=Lights.choices, default=Lights.LED)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
