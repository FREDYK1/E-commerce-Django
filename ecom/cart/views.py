from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_delete(request):
    pass

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for Post
    if request.POST.get("action") == "post":
        # Get id
        product_id = int(request.POST.get("product_id"))
        # lookup product with id
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product)

        # Get cart Quantity
        cart_quantity = cart.__len__()
        # Return Response
        response = JsonResponse({"qty": cart_quantity})
        return response

def cart_update(request):
    pass

