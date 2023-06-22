from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from encyclopedia import util, views



@csrf_exempt
def save_base(request, title=""):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        filename = request.POST.get('filename', None)

        if content:
            util.save_entry(filename, content)

def save_add(request, title=""):
    save_base(request, title)
    return redirect('/')

def save_edit(request, title=""):
    save_base(request, title)
    filename = request.POST.get('filename', None)
    return redirect(f"../../wiki/{filename}")

def edit(request, title):
    entry = util.get_entry(title)
    return render(request, 'edit.html', {"entry": entry.strip(), "title":title })

def add(request):
    #print(title)
    #if len(title) == 0:
    return render(request, 'add.html')
    # else:
    #     entry = util.get_entry(title)
    #     return render(request, 'edit.html', {"entry": entry})


# Create your views here.

