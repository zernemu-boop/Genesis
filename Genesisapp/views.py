from django.shortcuts import render
from Genesisapp.models import *

# Create your views here.
def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    
    if request.method == 'POST' :
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        mycontact.save()
        return render(request, 'index.html')
    
    else:
        return render(request, 'index.html')
    

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

