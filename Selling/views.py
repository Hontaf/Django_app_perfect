from django.shortcuts import render
from .models import Category
from django.views.generic import ListView

# Create your views here.
class CategoryView(ListView):
    model = Category
    template_name = "Category/home.html"