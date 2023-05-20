from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<marquee><h1>Srujana Thinnava Raa ,Em Raa Nannu Vadilesthunnava Em Em Em Natakalu Esthunnava........</h1></marquee>')


def revi(request):
    return HttpResponse("<h1><i>It's Not Ravi It's Revi</h1></i>")