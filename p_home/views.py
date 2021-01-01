from django.shortcuts import render
from .models import Info
# Create your views here.

def index(request):
    databa=Info.objects.get()
    print(databa.name)
    context={'info':databa}
    return render(request,'index.html',context)