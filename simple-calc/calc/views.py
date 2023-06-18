from django.shortcuts import render
from .functions.operations import Addition, Subtraction, Multiply, Division
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    if request.method == "POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        operation = request.POST["operation"]
        
        result = 0

        if operation == "+":
            result = Addition(num1, num2)
        elif operation == "-":
            result = Subtraction(num1, num2)
        elif operation == "*":
            result = Multiply(num1, num2)
        elif operation == "/":
            result = Division(num1, num2)
        
        success = "The result is " + str(result)

        return HttpResponse(success)
    return render(request, "index.html")

