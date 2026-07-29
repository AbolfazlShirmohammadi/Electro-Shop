from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from .models import Order, OrderItem
from django.db import transaction




@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created')

    return render(
        request,
        'order/html/my_orders.html',
        {
            'orders': orders
        }
    )






@login_required
@transaction.atomic
def create_order(request):

    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.items.exists():
        messages.error(request, "سبد خرید شما خالی است.")
        return redirect("cart")

    order = Order.objects.create(
        user=request.user
    )

    total = 0

    for item in cart.items.all():

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

        total += item.product.price * item.quantity

    order.total_price = total
    order.save()

   
    cart.items.all().delete()

    messages.success(request, "سفارش شما با موفقیت ثبت شد.")

    return redirect("my_orders")