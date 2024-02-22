from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Lamp
from .serializers import LampSerializer
from .permissions import IsOwnerOrReadOnly

class LampList(ListCreateAPIView):
  queryset = Lamp.objects.all()
  serializer_class = LampSerializer

class LampDetail(RetrieveUpdateDestroyAPIView):
  queryset = Lamp.objects.all()
  serializer_class = LampSerializer
  permission_classes = (IsOwnerOrReadOnly,)
