from django.shortcuts import render


def home_page(request):

    response = render(request, 'home.html')
    return response
