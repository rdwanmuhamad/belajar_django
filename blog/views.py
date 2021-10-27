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
        ],
        'banner' : 'blog/img/banner-2.jpg',
        'app_css' : 'blog/css/style.css',
        'logo' : 'img/fanta-logo.png',
    }
    return render(request, 'blog/index.html', context)