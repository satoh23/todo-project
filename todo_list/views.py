from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def share(ToDoList):
    share_text = "おはようございます！😆\n今日のやる事は\n\n"
    for ToDo in ToDoList:
        share_text += "✅ " + ToDo + "\n"
    share_text += "\nです!\n今日も1日頑張っていきましょう！🔥\n\n#駆け出しエンジニアと繋がりたい\n#今日の積み上げ\n"
    return share_text

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            item = share(List.objects.values_list('item', flat=True))
            messages.success(request, ('追加されました'))
            return render(request, 'home.html', {'all_items': all_items, 'item': item})
    else:
        all_items = List.objects.all
        item = share(List.objects.values_list('item', flat=True))
        return render(request, 'home.html', {'all_items': all_items, 'item': item})


def about(request):
    context = {'first_name': 'Harry', 'last_name': 'Potter'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('削除しました'))
    return redirect('home')

def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('編集しました'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
