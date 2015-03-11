from django.forms import widgets
from rest_framework import serializers

from finance.models import School, SECTOR_CHOICES, Loan, Grant

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'state', 'zip', 'sector')

class SchoolGrantSerializer(serializers.ModelSerializer):
    class Meta:
        grants = serializers.PrimaryKeyRelatedField(many=True, queryset=Grant.objects.all())

        model = School
        fields = ('id', 'grants')


class LoanSerializer(serializers.ModelSerializer):
    schools = serializers.PrimaryKeyRelatedField(many=True, queryset=School.objects.all())

    class Meta:
        model = Loan
        fields = ('id', 'schools','loan_type', 'recipients', 'number_of_loans',
                  'loan_money_originated','number_of_disbursements',
                  'loan_money_disbursed','year')

class GrantSerializer(serializers.ModelSerializer):
    # schools = serializers.PrimaryKeyRelatedField(many=True, queryset=School.objects.all())

    class Meta:
        model = Grant
        fields = ('id','grant_type', 'recipients', 'grant_money_disbursed', 'year')
