from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Count, Q

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):  # Změna názvu z 'login' na 'user_login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Použití auth_login místo login
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def user_logout(request):  # Změna názvu z 'logout' na 'user_logout'
    if request.user.is_authenticated:
        auth_logout(request)  # Použití auth_logout místo logout
    return redirect('login')


@login_required
def index(request):
    if request.method == 'POST':
        # Přidání nového úkolu
        text = request.POST.get('ukol')
        poznamka = request.POST.get('poznamka', '')
        ocekavane = request.POST.get('ocekavane') or None
        predmet = request.POST.get('predmet', '')
        
        if text:
            Todo.objects.create(
                user=request.user,  # Přidat uživatele
                text=text,
                poznamka=poznamka,
                ocekavane=ocekavane,
                predmet=predmet
            )
        return redirect('index')
    
    # Filtrovat pouze úkoly aktuálního uživatele
    todos = Todo.objects.filter(user=request.user, deleted=False).order_by('-created')
    return render(request, 'index.html', {'todos': todos})

@login_required
def done(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=pk, user=request.user)  # Přidat user filter
        todo.done = not todo.done
        if todo.done:
            todo.completed = timezone.now()
        else:
            todo.completed = None
        todo.save()
    return redirect('index')

@login_required
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)  # Přidat user filter
    todo.deleted = True
    todo.deleted_at = timezone.now()
    todo.save()
    return redirect('index')

@login_required
def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)  # Přidat user filter
    if request.method == 'POST':
        todo.text = request.POST.get('ukol', todo.text)
        todo.poznamka = request.POST.get('poznamka', todo.poznamka)
        ocekavane = request.POST.get('ocekavane')
        todo.ocekavane = ocekavane if ocekavane else None
        todo.predmet = request.POST.get('predmet', todo.predmet)
        todo.save()
        return redirect('index')
    return render(request, 'edit.html', {'todo': todo})

@login_required
def history(request):
    splnene = Todo.objects.filter(user=request.user, done=True, deleted=False).order_by('-completed')
    smazane = Todo.objects.filter(user=request.user, deleted=True).order_by('-deleted_at')
    return render(request, 'history.html', {'splnene': splnene, 'smazane': smazane})

@login_required
def admin_stats(request):
    """Admin view se statistikami všech uživatelů"""
    # Kontrola, zda je uživatel admin/staff
    if not request.user.is_staff:
        return redirect('index')  # Nebo vrátit 403 chybu
    
    # Získání statistik pro všechny uživatele
    users_stats = []
    for user in User.objects.all():
        stats = {
            'user': user,
            'aktivni': Todo.objects.filter(user=user, done=False, deleted=False).count(),
            'splnene': Todo.objects.filter(user=user, done=True, deleted=False).count(),
            'smazane': Todo.objects.filter(user=user, deleted=True).count(),
            'celkem': Todo.objects.filter(user=user).count(),
        }
        users_stats.append(stats)
    
    # Celkové statistiky
    total_stats = {
        'celkem_uzivatelu': User.objects.count(),
        'celkem_ukolu': Todo.objects.count(),
        'aktivni_ukoly': Todo.objects.filter(done=False, deleted=False).count(),
        'splnene_ukoly': Todo.objects.filter(done=True, deleted=False).count(),
        'smazane_ukoly': Todo.objects.filter(deleted=True).count(),
    }
    
    return render(request, 'admin_stats.html', {
        'users_stats': users_stats,
        'total_stats': total_stats
    })