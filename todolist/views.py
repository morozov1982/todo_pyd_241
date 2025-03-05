from django.shortcuts import render, redirect

from todolist.models import TodoList, Category


def redirect_view(request):
    return redirect('/category/')

def todo(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'Add' in request.POST:
            title = request.POST['description']
            date = request.POST['date']
            category = request.POST['category_select']
            content = title + '--' + date + ' ' + category
            todo = TodoList(title=title, content=content, due_date=date,
                            category=Category.objects.get(name=category))
            todo.save()
            return redirect('/todo')

        if 'Delete' in request.POST:
            checkedlist = request.POST.getlist('checkedbox')

            for i in range(len(checkedlist)):
                todo = TodoList.objects.filter(id=int(checkedlist[i]))
                todo.delete()

    context = {
        'todos': todos,
        'categories': categories,
    }

    return render(request, 'todo.html', context)

def category(request):
    pass
