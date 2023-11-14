from django.shortcuts import render


def mainblog(request):
    return render(request, 'blog.html')
