from rest_framework import serializers
from .models import Lamp

class LampSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "owner", "name", "light_type", "description", "created_at")
    model = Lamp
