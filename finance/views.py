from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from finance.models import School
from finance.serializers import SchoolSerializer


@api_view(['GET', 'POST'])
def school_list(request):
    """
    List all schools, or create a new school.
    """
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def school_detail(request, pk):
    """
    Retrieve, update or delete a school.
    """
    try:
        school = School.objects.get(pk=pk)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)