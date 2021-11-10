from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    # membuat query
    posts = Post.objects.all()
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
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)