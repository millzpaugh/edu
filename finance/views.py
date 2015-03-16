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


class SchoolList(APIView):
    """
    List all schools, or create a new school.
    """
    def get(self, request, format=None):
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDetail(APIView):
    """
    Retrieve, update or delete a school instance.
    """
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SchoolGrantList(APIView):
    """
    Retrieve all grants from a specific school instance.
    """
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        grants = Grant.objects.filter(school_id=school)
        serializer = GrantSerializer(grants, many=True)
        return Response(serializer.data)


class SchoolLoanList(APIView):
    """
    Retrieve all loans from a specific school.

    """
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        loans = Loan.objects.filter(school_id=school)
        serializer = LoanSerializer(loans, many=True, )
        return Response(serializer.data)

class SchoolHighlight(generics.GenericAPIView):
    queryset = School.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        school = self.get_object()
        return Response(school.highlight)


@api_view(('GET',))
def api_root(request, format=None):
    """
    Endpoints Available for Student Loan & Grant Data.
    (Currently, schools_url is the only navigable link from the API root page.)

    """
    return Response({
        'school_url':  'http://localhost:7000/schools/{school}/',
        'school_grants_url': 'http://localhost:7000/schools/{school}/grants/',
        'school_loans_url': 'http://localhost:7000/schools/{school}/loans/',
        'schools_url': reverse('school-list', request=request, format=format),
    })


#Convert to redis store before implementing these views to avoid socket error

# class GrantListByYear(APIView):
#     """
#     Retrieve all grants from a specific year.
#     """
#
#     def get(self, request, year, format=None):
#         grants = Grant.objects.filter(year=year)
#         serializer = GrantSerializer(grants, many=True)
#         return Response(serializer.data)
#
#
# class LoanListByYear(APIView):
#     """
#     Retrieve all loans from a specific year.
#     """
#
#     def get(self, request, year, format=None):
#         loans = Loan.objects.filter(year=year)
#         serializer = LoanSerializer(loans, many=True)
#         return Response(serializer.data)

class LoanDetail(APIView):
    """
    Retrieve, update or delete a school instance.
    """
    def get_object(self, pk):
        try:
            return Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan, context={'request': request})
        return Response(serializer.data)

class GrantDetail(APIView):
    """
    Retrieve, update or delete a school instance.
    """
    def get_object(self, pk):
        try:
            return Grant.objects.get(pk=pk)
        except Grant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grant = self.get_object(pk)
        serializer = GrantSerializer(grant, context={'request': request})
        return Response(serializer.data)