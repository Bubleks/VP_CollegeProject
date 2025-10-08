from django.shortcuts import render, HttpResponse
from .models import Title


def print_hello(request):
    return HttpResponse(request.method)

def test_templates(request):
    titles = Title.objects.all()
    return render(request, 'test.html',
                  {
                      'titles': titles
                  })

#def print_hello(request):
#    first = 10
#    second = 15
#    summary = first + second
#    return HttpResponse(request.GET[])
