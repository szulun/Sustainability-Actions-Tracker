from rest_framework import serializers
from .models import SustainabilityAction

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainabilityAction
        fields = '__all__' # auto catch id, action, date, points