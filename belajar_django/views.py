from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello World!")

# def about(request):
#     return HttpResponse("Hello About!")

def index(request):
    context = {
        'title' : 'Home | Belajar Django',
        'page'  : 'Home'
    }
    return render(request, 'index.html', context)

# def about(request):
#     return render(request, 'about.html')