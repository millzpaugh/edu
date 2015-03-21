from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from finance.models import School, Loan, Grant
from finance.serializers import SchoolSerializer, GrantSerializer, LoanSerializer


@api_view(('GET',))
def api_root(request, format=None):
    """
    Endpoints Available for Student Loan & Grant Data.

    """
    return Response({
        'schools_url': reverse('school-list', request=request, format=format),
        'grants_url': reverse('grant-list', request=request, format=format),
        'loans_url': reverse('loan-list', request=request, format=format),
    })


class SchoolList(generics.ListCreateAPIView):
    """
    List all schools, or create a new school.
    """
    model= School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()
        return queryset


class SchoolDetail(generics.ListAPIView):
    """
    Retrieve, update or delete a school instance.
    """
    model= School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return School.objects.filter(id=pk)


class SchoolGrantList(generics.ListAPIView):
    """
    Retrieve all grants from a specific school instance.
    """

    model= Grant
    serializer_class = GrantSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return Grant.objects.filter(school_id=pk)


class SchoolLoanList(generics.ListAPIView):
    """
    Retrieve all loans from a specific school.

    """
    model= Loan
    serializer_class = LoanSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return Loan.objects.filter(school_id=pk)

class SchoolHighlight(generics.GenericAPIView):
    queryset = School.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        school = self.get_object()
        return Response(school.highlight)

class LoanHighlight(generics.GenericAPIView):
    queryset = Loan.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        loan = self.get_object()
        return Response(loan.highlight)

class GrantHighlight(generics.GenericAPIView):
    queryset = Grant.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        grant = self.get_object()
        return Response(grant.highlight)

class LoanList(generics.ListCreateAPIView):
    """
    Retrieve all loans.
    """

    model= Loan
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = Loan.objects.all()
        return queryset

class GrantList(generics.ListCreateAPIView):
    """
    Retrieve all grants.
    """

    model= Grant
    serializer_class = GrantSerializer

    def get_queryset(self):
        queryset = Grant.objects.all()
        return queryset

class LoanDetail(generics.ListAPIView):
    """
    Retrieve, update or delete a loan instance.
    """
    model= Loan
    serializer_class = LoanSerializer

    def get_queryset(self):
        """

        """
        pk = self.kwargs['pk']
        return Loan.objects.filter(id=pk)

class GrantDetail(generics.ListAPIView):
    """
    Retrieve, update or delete a grant instance.
    """
    model= Grant
    serializer_class = GrantSerializer

    def get_queryset(self):
        """
        """
        pk = self.kwargs['pk']
        return Grant.objects.filter(id=pk)