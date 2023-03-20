from .models import Cart

def counter(request):
    cart_count=0
    if "admin" in request.path:
        return{}
    else:
        try:
            carts=Cart.objects.filter(user=request.user.id)
            for q in carts:
                cart_count+=q.quantity
        
        except Cart.DoesNotExist:
            cart_count=0
    
    return dict(cart_count=cart_count)
