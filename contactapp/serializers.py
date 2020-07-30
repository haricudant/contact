from rest_framework import serializers
from . import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'message', 'posted_at', 'name', 'number',)
        model = models.Contact
