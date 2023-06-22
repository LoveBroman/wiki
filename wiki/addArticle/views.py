from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from encyclopedia import util, views



@csrf_exempt
def save(request, title=""):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        filename = request.POST.get('filename', None)

        if content:
            util.save_entry(filename, content)

        if len(title) == 0:
            return redirect('/')
        else:
            redirect(f"/{filename}")

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

