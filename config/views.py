from django.http import HttpResponse
from django.shortcuts import render
from visitor.models import Visitor

def main(request):
    return render(request, "main.html")
