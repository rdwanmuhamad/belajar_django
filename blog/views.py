from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    # membuat query
    posts = Post.objects.all()
    print(posts)
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

def berita(request):
    # membuat query
    posts = Post.objects.filter(category='berita')
    print(posts)
    context = {
        'title' : 'Blog | Belajar Django',
        'page'  : 'Berita',
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

def olahraga(request):
    # membuat query
    posts = Post.objects.filter(category='olahraga')
    print(posts)
    context = {
        'title' : 'Blog | Belajar Django',
        'page'  : 'Olahraga',
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