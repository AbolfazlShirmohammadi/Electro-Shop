from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from product.models import Product




@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    context = {
        'cart': cart,
        'items': items,
        'total': cart.total_price()
    }

    return render(
        request,
        'cart/html/cart.html',
        context
    )



@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.method == 'POST':
        return JsonResponse({'status': 'success', 'message': 'محصول به سبد اضافه شد'})

   
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))



@login_required
def remove_from_cart(request, id):

    cart = get_object_or_404(
        Cart,
        user=request.user
    )


    item = get_object_or_404(
        CartItem,
        id=id,
        cart=cart
    )


    item.delete()


    return redirect('cart')



@login_required
def increase_quantity(request, id):

    item = get_object_or_404(
        CartItem,
        id=id,
        cart__user=request.user
    )


    item.quantity += 1
    item.save()


    return redirect('cart')



@login_required
def decrease_quantity(request, id):

    item = get_object_or_404(
        CartItem,
        id=id,
        cart__user=request.user
    )


    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    else:
        item.delete()


    return redirect('cart')



