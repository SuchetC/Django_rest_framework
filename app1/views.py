from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet, ModelViewSet


# we can implement 2 types of viewset 1> ViewSet 2>ModelViewSet
#  This cls for ModelViewSET It automatically generate urls
class StudViewset(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer



# This cls for ViewSet here we should explicitly write list(),retrive() etc funs

"""
class StudViewset(ViewSet): 

    def list(self,request):
        stud = Students.objects.all()
        serializer = StudentSerializer(stud , many=True)
        return Response(serializer.data)

    def retrive(self,request,pk):
        stud = Students.objects.get(pk=pk)
        serializer = StudentSerializer(stud)
        return Response(serializer.data , request.data)

"""







# these cls implemented to just understanging request methods in rest_framework
"""
class StudView(APIView):
    def get(self, request, *args, **kwargs):
        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

class StudentView(APIView):


    def get(self, request, id):
        result = Students.objects.get(id=id)
        if id:
            serializers = StudentSerializer(result)
            return Response({'status': 'success', "students": serializers.data}, status=200)

        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True,data=request.data)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        result = Students.objects.get(id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        result = get_object_or_404(Students, id=id)
        result.delete()

"""