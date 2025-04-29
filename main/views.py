from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.db.models import Q


def catalog(request):
    category = request.GET.get('category', '')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'main/catalog.html', {'products': products, 'categories': categories})


def catalog_table(request):
    category = request.GET.get('category', '')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    return render(request, 'main/partials/table.html', {'products': products})


def search(request):
    return render(request, 'main/search.html')


def search_results(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )[:5] 
    return render(request, 'main/partials/search_results.html', {'products': products})


def modal(request):
    products = Product.objects.all()
    return render(request, 'main/modal.html', {'products': products})


def modal_content(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'main/partials/modal_content.html', {'product': product})


def close_modal(request):
    return HttpResponse('<div id="modal" style="display: none;"></div>')