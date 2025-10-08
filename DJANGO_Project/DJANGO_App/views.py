from django.shortcuts import render, HttpResponse
from .models import Title


def print_hello(request):
    return HttpResponse(request.method)

def test_templates(request):
    titles = Title.object.all()
    return render(request, 'test.html',
                  {
                      'my_titles': titles
                  })

#def print_hello(request):
#    first = 10
#    second = 15
#    summary = first + second
#    return HttpResponse(request.GET[])
