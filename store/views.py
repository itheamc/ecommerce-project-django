from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from ecommerce_project import settings
from .models import *


# Create your views here.


def stores(request):
    data = Store.objects.all()
    return render(request, 'stores.html', {'stores': data})


def store(request, store_id):
    try:
        data = Product.objects.filter(store__id=store_id)
        return render(request, 'store.html', {'products': data})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def product(request, product_id):
    try:
        data = Product.objects.get(id=product_id)
        return render(request, 'product.html', {'product': data})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def category(request, category_id):
    try:
        data = Category.objects.get(id=category_id)
        return render(request, 'category.html', {'category': data})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def cart(request):
    send_mail(subject='Warning!!', message='Your account is in risk!!', from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=['abiralc27@gmail.com'])
    return JsonResponse({'message': 'from cart'})
