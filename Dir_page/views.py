from django.shortcuts import render
from .models import Director
# Create your views here.
def director(request):
    
        
    return render(request, 'director.html')