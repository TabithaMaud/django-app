from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.


def book_list(request):
    data = Book.objects.all()
    data = list(data.values())
    return JsonResponse(data, safe=False)
