from django.http import HttpResponse

def home(request):
    domain = request.get_host()

    if "xyz.com" in domain:
        return HttpResponse("<h1>Welcome to XYZ site</h1>")
    elif "abcc.com" in domain:
        return HttpResponse("<h1>Welcome to ABCC site</h1>")
    else:
        return HttpResponse("<h1>Default site</h1>")
