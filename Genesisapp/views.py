from django.shortcuts import render

# Create your views here.
def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

