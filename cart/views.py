from django.shortcuts import render, redirect

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
    # Get the cart variable if already exists in the session else create one 
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # Update cart quantity if cart already exists
        cart[item_id] += quantity
    else:
        # Add item to the cart
        cart[item_id] = quantity
    
    # Override the variable in the session with the updated cart
    request.session['cart'] = cart
    return redirect(redirect_url)
    
