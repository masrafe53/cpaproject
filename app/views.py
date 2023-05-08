from django.shortcuts import render
from .models import offer
# Create your views here.
def home(request):
    offers = offer.objects.all()
    return render(request,'index.html',{'offers': offers})