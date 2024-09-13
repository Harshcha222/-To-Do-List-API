from .views import get_todos, modify_todo
from django.urls import path

urlpatterns = [
    path('todos/', get_todos, name='get_todos'),      
            
  
    path('todos/<int:id>/', modify_todo, name='modify_todo'),   
]

