from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from shop import models
from .cart import Cart
from . import forms


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    form = forms.CartAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product, product_count=form_data['product_count'], update_count=form_data['update'])
    return redirect(reverse('cart:cart_details'))


def CartDetails(request):
    cart = Cart(request)
    for item in cart:
        item['update_product_count_form'] = forms.CartAddProductForm(
            initial={'product_count': item['product_count'],
                     'update': True}
        )
    return render(request, 'cart/details.html', {'cart': cart})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    cart.remove(product)
    return redirect(reverse('cart:cart_details'))
