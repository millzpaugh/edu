from django.forms import widgets
from djangorestframework import serializers
from rest_framework import serializers

from finance.models import School, SECTOR_CHOICE

class SchoolSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=300)
    state = serializers.CharField(required=True, allow_blank=False, max_length=15)
    zip = serializers.IntegerField(required=True, allow_blank=False)
    sector = serializers.ChoiceField(choices=SECTOR_CHOICE)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.sector = validated_data.get('sector', instance.sector)
        instance.save()
        return instance
