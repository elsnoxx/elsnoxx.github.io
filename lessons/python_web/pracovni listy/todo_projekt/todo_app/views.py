from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        # Přidání nového úkolu
        text = request.POST.get('ukol')
        poznamka = request.POST.get('poznamka', '')
        ocekavane = request.POST.get('ocekavane') or None
        predmet = request.POST.get('predmet', '')
        
        if text:
            Todo.objects.create(
                text=text,
                poznamka=poznamka,
                ocekavane=ocekavane,
                predmet=predmet
            )
        return redirect('index')
    
    todos = Todo.objects.filter(deleted=False).order_by('-created')
    return render(request, 'index.html', {'todos': todos})

def done(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=pk)
        todo.done = not todo.done
        if todo.done:
            todo.completed = timezone.now()
        else:
            todo.completed = None
        todo.save()
    return redirect('index')

def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.deleted = True
    todo.deleted_at = timezone.now()
    todo.save()
    return redirect('index')

def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.text = request.POST.get('ukol', todo.text)
        todo.poznamka = request.POST.get('poznamka', todo.poznamka)
        ocekavane = request.POST.get('ocekavane')
        todo.ocekavane = ocekavane if ocekavane else None
        todo.predmet = request.POST.get('predmet', todo.predmet)
        todo.save()
        return redirect('index')
    return render(request, 'edit.html', {'todo': todo})

def history(request):
    splnene = Todo.objects.filter(done=True, deleted=False).order_by('-completed')
    smazane = Todo.objects.filter(deleted=True).order_by('-deleted_at')
    return render(request, 'history.html', {'splnene': splnene, 'smazane': smazane})