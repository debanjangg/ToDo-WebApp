from django.shortcuts import render, redirect
from .models import ToDo
from .forms import AddToDo

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html', {"items": ToDo.objects.all(), "form": AddToDo()})
    if request.method == "POST":
        form = AddToDo(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)

def del_ToDo(request, pk):
    obj = ToDo.objects.get(id=pk)
    obj.delete()
    return redirect(home)