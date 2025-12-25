from rest_framework import viewsets
from .models import SustainabilityAction
from .serializers import ActionSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = SustainabilityAction.objects.all()
    serializer_class = ActionSerializer