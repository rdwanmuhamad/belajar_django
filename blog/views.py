from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Blog | Belajar Django',
        'page'  : 'Blog',
        'nav'   : [
                    ['/' , 'Home'],
                    ['/blog' , 'Blog'],
                    ['/about' , 'About'],
        ]
    }
    return render(request, 'blog/index.html', context)