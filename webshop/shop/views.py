from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . import models
from cart.forms import CartAddProductForm
from cart.cart import Cart
from zeep import Client

def ShopView(request):
    product_list = models.Product.objects.all()[:5]
    return render(request, 'index.html', {'product_list': product_list})


@login_required
def CheckoutView(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = models.Order.objects.create(customer=request.user)
        for item in cart:
            models.OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            product_price=item['price'],
                                            product_count=item['product_count'],
                                            product_cost=Decimal(item['product_count']) * Decimal(item['price']))
        return render(request, 'order_detail.html', {'order': order})
    return render(request, 'checkout.html', {'cart': cart})


def StoreView(request):
    return render(request, 'store.html')


def ProductView(request, pk):
    product_detail = get_object_or_404(models.Product, id=pk)
    cart_add_product_form = CartAddProductForm()
    return render(request, 'product.html',
                  {'product_detail': product_detail, 'cart_add_product_form': cart_add_product_form})


merchant = '*************************'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')


def to_bank(request, order_id):
    order = get_object_or_404(models.Order, id=order_id)
    amount = 0
    order_items = models.OrderItem.objects.filter(order=order)
    for item in order_items:
        amount += item.product_cost
    callbackUrl = 'http://127.0.0.1:8000/callback/'
    mobile = ''
    email = ''
    description = 'test'
    result = client.service.PaymentRequest(merchant, mobile, email, description, CallbackURL=callbackUrl)

    if result.Status == 100 and len(result.Authority) == 36:
        models.Invoice.objects.create(order=order, authority=result.Authority)
        return redirect('https://www.zarinpal.com/pg/StartPay/') + result.Authority
    else:
        return HttpResponse('error' + str(result.Status))


def callback(request):
    if request.GET.get('Status')=='OK':
        authority=request.GET.get('Authority')
        invoice=get_object_or_404(models.Invoice, authority=authority)
        amount = 0
        order = invoice.order
        order_items = models.OrderItem.objects.filter(order=order)
        for item in order_items:
            amount += item.product_cost
        result = client.service.PaymentVerification(merchant, authority, amount)
        if result.Status==100:
            return render(request, 'callback.html', {'invoice': invoice})
        else:
            return HttpResponse('error' + str(result.Status))
    else:
        return HttpResponse('error')
