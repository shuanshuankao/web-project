from django.shortcuts import render
from .models import Todo

# Create your views here.
def todolist(request):
    todos=Todo.objects.all()
    result={"todos":todos}
    return render(request,"todo/todolist.html",result)