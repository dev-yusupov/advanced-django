from django.shortcuts import render
from .models import Animal
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        name = request.POST["name"]

        new_animal = Animal(name=name)
        new_animal.save()

        success = f"Animal: {name.upper()} is successfully created!"

        return HttpResponse(success)