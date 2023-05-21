from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .utils import common_function
# Create your views here.

def LoginResponse(request):
    if request.method = 'Data':
        PassCode = request.Data["password"]
        Username = request.Data["username"]
        permission = checkUser(request, Username=Username, PassCode=PassCode)
        if permission == True:
            index(request, permission);
        else:

    return render(request."index.html")