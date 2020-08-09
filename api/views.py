from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from api.models import ToDo
from api.serializers import apiSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST','DELETE'])
def tlist(request):
	todo = ToDo.objects.all()
	if request.method == 'GET':
		todo_serializer = apiSerializer(todo,many=True)
		return JsonResponse(todo_serializer.data,safe=False)
			
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		todo_serializer = apiSerializer(data=data)
		if todo_serializer.is_valid():
			todo_serializer.save()
			return JsonResponse(todo_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	
	elif request.method =='DELETE':
		count = todo.delete()
		return JsonResponse(f"{'message:' '{count[0]} Todo deleted successfully'}",status=status.HTTP_204_NO_CONTENT) 
		
	
@api_view(['GET','PUT','DELETE'])	
def todo_detail(request, id):
	todo = ToDo.objects.get(pk=id)
	if request.method =='GET':
		todo_serializer = apiSerializer(todo)
		return JsonResponse(todo_serializer.data, safe=False)
	
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		todo_serializer = apiSerializer(todo, data=data)
		if todo_serializer.is_valid():
			todo_serializer.save()
			return JsonResponse(todo_serializer.data, safe=False)
		return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	
	elif request.method == 'DELETE':
		todo.delete()
		return JsonResponse({'message':'Todo deleted'},status=status.HTTP_204_NO_CONTENT)

		

@api_view(['GET'])	
def allUsers_todo(request):
	todo = Todo.objects.all()
	
	if request.method== 'GET':
		todo_serializer = apiSerializer(todo,many=True)
		return JsonResponse(todo_serializer.data, safe=False)