from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the Home page!")

def about(request):
    return HttpResponse("Hello, this is the About page!")

def services(request):
    return HttpResponse("Hello, these are our Services!")

def projects(request):
    return HttpResponse("Hello, this is the Projects page!")

def contact(request):
    return HttpResponse("Hello, this is the Contact page!")

def blog(request):
    return HttpResponse("Hello, welcome to the Blog page!")

def team(request):
    return HttpResponse("Hello, meet our Team!")

def portfolio(request):
    return HttpResponse("Hello, this is the Portfolio page!")

def career(request):
    return HttpResponse("Hello, this is the Career page!")

def feedback(request):
    return HttpResponse("Hello, this is the Feedback page!")
