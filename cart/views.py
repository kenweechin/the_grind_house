from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart content page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """

    product = get_object_or_404(Product, pk=item_id)
    # Get the quantity from the form and convert it to integer from string
    quantity = int(request.POST.get('quantity'))
    # Get the redirect url from the form
    redirect_url = request.POST.get('redirect_url')
    volume = None
    if 'product_volume' in request.POST:
        volume = request.POST['product_volume']
    # Get the cart variable if already exists in the session else create one
    cart = request.session.get('cart', {})

    if volume:
        # Check if the item is in the cart already
        if item_id in list(cart.keys()):
            # Check if another item of the samd id and same volume exists
            if volume in cart[item_id]['items_by_volume'].keys():
                # Then increment the quantity for that volume
                cart[item_id]['items_by_volume'][volume] += quantity
                messages.success(request,
                                 f'Updated volume {volume}ml {product.name}'
                                 f'quantity to'
                                 f'{cart[item_id]["items_by_volume"][volume]}')
            else:
                # Set equal to the quantity which is a new volume
                cart[item_id]['items_by_volume'][volume] = quantity
                messages.success(request,
                                 f'Added volume {volume}ml'
                                 f'{product.name} to your cart')
        else:
            # Add the item if is not in the cart
            cart[item_id] = {'items_by_volume': {volume: quantity}}
            messages.success(request,
                             f'Added volume {volume}ml {product.name}'
                             f'to your cart')
    else:
        if item_id in list(cart.keys()):
            # Update cart quantity if cart already exists
            cart[item_id] += quantity
        else:
            # Add item to the cart
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    # Override the variable in the session with the updated cart
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust cart quantity """

    product = get_object_or_404(Product, pk=item_id)

    # Get the quantity from the form and convert it to integer from string
    quantity = int(request.POST.get('quantity'))
    volume = None
    if 'product_volume' in request.POST:
        volume = request.POST['product_volume']
    # Get the cart variable if already exists in the session else create one
    cart = request.session.get('cart', {})

    if volume:
        if quantity > 0:
            cart[item_id]['items_by_volume'][volume] = quantity
            messages.success(request,
                             f'Updated volume {volume}ml {product.name}'
                             f'quantity to'
                             f'{cart[item_id]["items_by_volume"][volume]}')
        else:
            del cart[item_id]['items_by_volume'][volume]
            if not cart[item_id]['items_by_volume']:
                cart.pop(item_id)
            messages.success(request,
                             f'Removed volume {volume}ml {product.name}'
                             f'from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request,
                             f'Updated {product.name} quantity to'
                             f'{cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    # Override the variable in the session with the updated cart
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_cart(request, item_id):
    """ Remove cart quantity """

    try:
        product = get_object_or_404(Product, pk=item_id)
        volume = None
        if 'product_volume' in request.POST:
            volume = request.POST['product_volume']
        # Get cart variable if already exists in the session else create one
        cart = request.session.get('cart', {})

        if volume:
            del cart[item_id]['items_by_volume'][volume]
            if not cart[item_id]['items_by_volume']:
                cart.pop(item_id)
            messages.success(request,
                             f'Removed volume {volume}ml {product.name}'
                             f'from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        # Override the variable in the session with the updated cart
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
