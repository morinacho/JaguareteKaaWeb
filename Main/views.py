from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Main/index.html')

def aboutus(request):
    return render(request, 'Main/aboutus.html')

def contact(request):
    return render(request, 'Main/contact.html')

def newproduct(request):
    return render(request, 'Main/newproduct.html')