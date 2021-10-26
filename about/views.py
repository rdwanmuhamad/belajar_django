from django.shortcuts import render

def index(request):
    context = {
        'title' : 'About | Belajar Django',
        'page'  : 'About'
    }
    return render(request, 'about/index.html', context)