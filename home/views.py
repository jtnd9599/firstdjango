from django.shortcuts import render
from .forms import customForms

# Create your views here.


def home_view(request):
    return render(request,"newwebpage.html")
    
def merit(request):
    return render(request,"merit.html")


def success(request):
    return render(request,"success.html")

def form_view(request):
    form=customForms()
    context={
        "head":'custom forms created here',
        "forms":form
    }
    return render(request,'forms.html',context)
    
 