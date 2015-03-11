from django.forms import widgets
from rest_framework import serializers

from finance.models import School, SECTOR_CHOICES

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'state', 'zip', 'sector')
