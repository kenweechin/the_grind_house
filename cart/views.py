from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart content page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """

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
            # Check if another item of the samd id and same volume exists already
            if volume in cart[item_id]['items_by_volume'].keys():
                # Then increment the quantity for that volume
                cart[item_id]['items_by_volume'][volume] += quantity
            else:
                # Or else set equal to the quantity which is a new volume for the item
                cart[item_id]['items_by_volume'][volume] = quantity
        else: 
            # Add the item if is not in the cart
            cart[item_id] = {'items_by_volume': {volume: quantity}}
    else:
        if item_id in list(cart.keys()):
            # Update cart quantity if cart already exists
            cart[item_id] += quantity
        else:
            # Add item to the cart
            cart[item_id] = quantity
    
    # Override the variable in the session with the updated cart
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust cart quantity """

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
        else:
            del cart[item_id]['items_by_volume'][volume]
            if not cart[item_id]['items_by_volume']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id) 
    
    # Override the variable in the session with the updated cart
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_cart(request, item_id):
    """ Remove cart quantity """

    try:
        volume = None
        if 'product_volume' in request.POST:
            volume = request.POST['product_volume']
        # Get the cart variable if already exists in the session else create one 
        cart = request.session.get('cart', {})

        if volume: 
            del cart[item_id]['items_by_volume'][volume]
            if not cart[item_id]['items_by_volume']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)  
        
        # Override the variable in the session with the updated cart
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        print(f"ERROR: {e}")
        return HttpResponse(status=500)
