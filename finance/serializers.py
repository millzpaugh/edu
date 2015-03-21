from django.forms import widgets
from rest_framework import serializers
from rest_framework.reverse import reverse


from finance.models import School, SECTOR_CHOICES, Loan, Grant


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='school-highlight', format='html')
    loans = serializers.HyperlinkedRelatedField(source='id',read_only=True,view_name='school-loan-list')
    grants = serializers.HyperlinkedRelatedField(source='id',read_only=True,view_name='school-grant-list')

    class Meta:
        model = School
        fields = ('id', 'name', 'state', 'zip', 'sector','url','loans','grants')

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='loan-highlight', format='html')

    class Meta:
        model = Loan
        fields = ('id', 'school_id','loan_type', 'recipients', 'number_of_loans',
                  'loan_money_originated','number_of_disbursements',
                  'loan_money_disbursed','year', 'url')


class GrantSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='grant-highlight', format='html')

    class Meta:
        model = Grant
        fields = ('id','school_id','grant_type', 'recipients', 'grant_money_disbursed', 'year', 'url')
