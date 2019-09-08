from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)


