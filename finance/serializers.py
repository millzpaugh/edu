from django.forms import widgets
from rest_framework import serializers

from finance.models import School, SECTOR_CHOICES, Loan, Grant

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='school-highlight', format='html')

    class Meta:
        model = School
        fields = ('id', 'name', 'state', 'zip', 'sector')


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'loan_type', 'recipients', 'number_of_loans',
                  'loan_money_originated','number_of_disbursements',
                  'loan_money_disbursed','year')

class GrantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Grant
        fields = ('id','grant_type', 'recipients', 'grant_money_disbursed', 'year')
