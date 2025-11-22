import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request, id):
    item = get_object_or_404(Item, pk=id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=settings.DOMAIN + '/success',
        cancel_url=settings.DOMAIN + '/cancel',
    )
    return JsonResponse({'id': session.id})


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item.html', {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'order.html', {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


def buy_order(request, id):
    order = get_object_or_404(Order, id=id)
    line_items = []
    for oi in order.orderitem_set.all():
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': oi.item.name},
                'unit_amount': oi.item.price,
            },
            'quantity': oi.quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=settings.DOMAIN + '/success/',
        cancel_url=settings.DOMAIN + '/cancel/',
    )
    return JsonResponse({'id': session.id})