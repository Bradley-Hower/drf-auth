from django.urls import path
from .views import LampList, LampDetail

urlpatterns = [
  path("", LampList.as_view(), name="lamp_list"),
  path("<int:pk>/", LampDetail.as_view(), name="lamp_detail"),
]
