from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "MINOR PROJECT"
    }
    return render(request, 'equipments/home.html', context)

