import form as form
from django.shortcuts import render, HttpResponse

from products.models import Product
from feedback.models import Feedback


def feedback(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['text']
    element = Feedback(user_name=name, email=email, message=message)
    element.save()
    return render(request, 'feedback.html')


def main_page(request):
    return render(request, 'index.html')


def pillows(request):
    return render(request, 'pillows.html', {'products': Product.objects.all()})


def mattresses(request):
    return render(request, 'mattresses.html', {'products': Product.objects.all()})


def contacts(request):
    return render(request, 'contacts.html')


def cart(request):
    return render(request, 'cart.html')


def product(request, prod_id):
    prod = Product.objects.get(id=prod_id)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)

