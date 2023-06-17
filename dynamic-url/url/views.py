from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def show(request, name):
    name = name.capitalize()
    return render(request, "show.html", {
        "name": name
    })