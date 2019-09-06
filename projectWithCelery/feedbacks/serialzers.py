from .models import EmailCreator
from rest_framework import serializers


class EmailCreatorSer(serializers.Serializer):
    class Meta:
        fields = ("__all__")
        model = EmailCreator
