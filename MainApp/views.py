from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'MainApp/main.html')


# def contact(request):
#     return render(request, 'MainApp/basic.html', {'values': ['Если остались вопросы:', '+799999999']})
