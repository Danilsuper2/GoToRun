from django.contrib import messages
from django.shortcuts import render


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        print(request.POST)
        messages.success(request, 'Profile updated successfully')