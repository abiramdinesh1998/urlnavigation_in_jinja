from django.shortcuts import render

# Create your views here.
def navigation_1(request):
    return render(request,'navigation_1.html')

def navigation_2(request):
    return render(request,'navigation_2.html')
