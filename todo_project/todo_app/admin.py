from django.contrib import admin
from todo_app.models import Todo

class TodoDataAdmin(admin.ModelAdmin):
     list_display = ('title', 'description', 'completed')

admin.site.register(Todo,TodoDataAdmin)




# Register your models here.
