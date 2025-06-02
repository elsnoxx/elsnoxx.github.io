Úkolníček – Domácí úkol
Vytvoř v Django jednoduchou webovou aplikaci Úkolníček, která slouží k evidenci úkolů.

🎯 Zadání
Tvoje aplikace by měla umět:
✅ Vkládat nové úkoly
✅ Vypsat všechny úkoly
✅ Upravit existující úkol
✅ Odstranit úkol

🗂️ Model Úkol
V souboru models.py vytvoř následující model:

python
Copy
Edit
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
🌐 Views
V souboru views.py vytvoř následující view funkce:

python
Copy
Edit
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST['due_date']
        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.due_date = request.POST['due_date']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
🖼️ HTML šablony
💡 Doporučené šablony:

task_list.html – vypíše seznam všech úkolů

task_form.html – formulář pro přidání nebo úpravu úkolu

task_confirm_delete.html – potvrzení smazání úkolu

(Pokud budeš chtít, můžu dodat i ukázkové šablony.)

✨ Bonusové úkoly
✅ Přidat možnost označit úkol jako dokončený (checkbox)
✅ Využít admin rozhraní (python manage.py createsuperuser a úpravy v admin.py)
✅ Přidat filtr na splněné/nesplněné úkoly v seznamu

🔨 Co odevzdat
✅ Kompletní projektový adresář (nebo odkaz na GitHub)
✅ Screenshot funkční aplikace (běžící server, výpis úkolů)
✅ Screenshot admin rozhraní s přidaným modelem
✅ Krátký popis projektu (co jsi vytvořil, jak aplikace funguje)

🚀 Začátek
bash
Copy
Edit
# vytvoření projektu
django-admin startproject ukolnicek

# přidání aplikace
python manage.py startapp tasks

# přidání aplikace do settings.py
INSTALLED_APPS = [
    ...
    'tasks',
]
Nezapomeň spustit:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
📌 Poznámka
Pokud bys potřeboval pomoct s šablonami, admin rozhraním nebo URL konfigurací, ozvi se! 💪

