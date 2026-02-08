from django.shortcuts import render

posts = [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27 2018'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 28 2018'
    },
    {
        'author':'Joe Joestar',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date_posted': 'August 27 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})