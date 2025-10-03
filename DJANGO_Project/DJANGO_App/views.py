from django.shortcuts import render, HttpResponse

def print_hello(request):
    return HttpResponse(request.method)

#def print_hello(request):
#    first = 10
#    second = 15
#    summary = first + second
#    return HttpResponse(request.GET[])
