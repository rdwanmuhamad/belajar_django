from django.shortcuts import render

def index(request):
    context = {
        'title' : 'About | Belajar Django',
        'page'  : 'About',
        'nav'   : [
                    ['/' , 'Home'],
                    ['/blog' , 'Blog'],
                    ['/about' , 'About'],
        ],
        'banner' : 'about/img/banner-3.jpg',
        'app_css' : 'about/css/style.css',
    }
    return render(request, 'about/index.html', context)