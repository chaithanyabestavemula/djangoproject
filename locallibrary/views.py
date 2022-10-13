from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import orders,product



def home(request):
    post=product.objects.all()

    return render(request,'base.html',{'post':post})
def demo(request):
    return HttpResponse("this is demo")

