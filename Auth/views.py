from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'Auth/login.html')

def register(request):
    return render(request, 'Auth/register.html')