from .cart import Cart

# Add the cart to the context
def cart(request):
    # Return the default data from our Cart
    return {"cart": Cart(request)}