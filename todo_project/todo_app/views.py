from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from todo_app.models import Todo 
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.decorators.http import require_http_methods
import json

from todo_app.serializer import TodoSerializer


@csrf_exempt
@require_http_methods(["GET", "POST"])
def get_todos(request, id=None):
    try:
        if request.method == 'GET':
            todos = Todo.objects.all().values('id', 'title', 'description', 'completed')
            return JsonResponse(list(todos), safe=False)

        elif request.method == 'POST':
            data = json.loads(request.body)
            serializer = TodoSerializer(data=data)

            if serializer.is_valid():
                todo = Todo.objects.create(
                    title=data.get('title'),
                    description=data.get('description'),
                    completed=data.get('completed')
                )
                return JsonResponse({
                    'id': todo.id,
                    'title': todo.title,
                    'description': todo.description,
                    'completed': todo.completed
                })
            else:
                return JsonResponse(serializer.errors, status=400)

    except KeyError:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
def modify_todo(request, id):
    try:
        if request.method == 'PUT':
            try:
                todo = Todo.objects.get(id=id)
                data = json.loads(request.body)
                serializer = TodoSerializer(data=data)

                if serializer.is_valid():
                    todo.title = data.get('title', todo.title)
                    todo.description = data.get('description', todo.description)
                    todo.completed = data.get('completed', todo.completed)
                    todo.save()
                    return JsonResponse({'message': 'Todo updated successfully'})
                else:
                    return JsonResponse(serializer.errors, status=400)

            except Todo.DoesNotExist:
                return JsonResponse({'error': 'Todo not found'}, status=404)

        elif request.method == 'DELETE':
            try:
                todo = Todo.objects.get(id=id)
                todo.delete()
                return JsonResponse({'message': 'Todo deleted successfully'})
            except Todo.DoesNotExist:
                return JsonResponse({'error': 'Todo not found'}, status=404)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': 'Invalid data'}, status=400)
