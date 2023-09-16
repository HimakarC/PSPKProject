from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def main(request):
    return render(request, 'all.html')