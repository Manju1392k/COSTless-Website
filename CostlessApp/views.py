from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Allitems(request):
    return render(request, 'allitems.html')

def Acer(request):
    return render(request, 'nitro.html')
