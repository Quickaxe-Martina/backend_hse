from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from . import models
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class TaskSerializer(ModelSerializer):
    
    class Meta:
        model = models.TodoModel
        fields = (
            'id',
            'name',
            'description',
            'is_done',
            'priority'
        )
        read_only_fields = ('id',)


class TaskListAPIView(APIView):
    http_method_names = ('get', 'post')

    def get(self, request):
        qs = models.TodoModel.objects.all().order_by(('priority'))
        return Response(data=TaskSerializer(qs, many=True).data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class TaskDetailAPIView(APIView):
    http_method_names = ('get', 'put', 'delete')

    def get(self, request, pk):
        task = get_object_or_404(models.TodoModel, pk=pk)
        return Response(data=TaskSerializer(task).data)
    
    def put(self, request, pk):
        task = get_object_or_404(models.TodoModel, pk=pk)
        serializer = TaskSerializer(data=request.data, instance=task)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, pk):
        models.TodoModel.objects.filter(pk=pk).delete()
        return Response(status=204)