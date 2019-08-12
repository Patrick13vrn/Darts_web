from django.shortcuts import render


def posts_list(request):
    n = ['Сергей', 'Дмитрий', 'Алексей']
    return render(request, 'blog/index.html', context={'names': n})
