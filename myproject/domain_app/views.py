from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    if request.site_name == "xyz":
        return HttpResponse("<h1>Welcome to XYZ site through middleware</h1>")
    elif request.site_name == "abcc":
        return HttpResponse("<h1>Welcome to ABCC site through middleware</h1>")
    else:
        return render(request, "default_home.html")
