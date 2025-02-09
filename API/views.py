
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    data = {
        "message":f"Hello {request.user.first_name}, welcome to your user area"
    }
    return Response(data)

def login_user(request):
    if request.method == "POST":
       
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("login_user") 
    return render(request,"login.html")