from django.shortcuts import render,redirect
from .models import Product,Customer, OrderPlaced,Cart
from .forms import MyRegistrationForm,MyCustomerForm
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    mobiles= Product.objects.filter(category="M")
    laptops= Product.objects.filter(category="L")
    bottom_wears= Product.objects.filter(category="BW")
    top_wears= Product.objects.filter(category="TW")
    context={"mobiles":mobiles,"laptops":laptops,
            "bottom_wears":bottom_wears, "top_wears":top_wears}
    return render(request,"app/home.html", context)

def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    
    return render(request, "app/productdetail.html",{"product":product})

@login_required
def add_to_cart(request):
    user=request.user
    item_already_in_cart1 = False
    product_id=request.GET.get("prod_id")
    print(product_id)
    product=Product.objects.get(id=product_id)
    print(product)
    item_already_in_cart1 = Cart.objects.filter(Q(product=product) & Q(user=request.user)).exists()
    if item_already_in_cart1 == False:
        Cart(product=product,user=user).save()
        return redirect("/cart")
    else:
        return redirect("/cart")
@login_required       
def show_cart(request):
    if request.user.is_authenticated:
        carts=Cart.objects.filter(user=request.user)
        amount=0.0
        shipping_amount=50
        totalamount=0.0
        cart_product=[]
        for p in carts:
            cart_product.append(p)
        
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount+=tempamount

            totalamount=amount+shipping_amount
            context={"carts":carts, "totalamount":totalamount,
                "shipping_amount":shipping_amount, "amount":amount}
            return render(request, "app/showcart.html",context)
        else:
            return render(request,"app/showcart.html",{"carts":carts})
        

@login_required
def plus_cart(request,pk):
    
    product=Product.objects.get(id=pk)
    c=Cart.objects.get(Q(product=product) & Q(user=request.user))
    c.quantity+=1
    c.save()

    carts=Cart.objects.filter(user=request.user)
    amount=0.0
    shipping_amount=50.0
    totalamount=0.0
    cart_product=[]
    for p in carts:
        cart_product.append(p)
    if cart_product:
        for p in cart_product:
            temp_amount=(p.quantity * p.product.discounted_price)
            amount+=temp_amount
        totalamount=amount+shipping_amount
        context={
            "carts":carts,
            "quantity":c.quantity,
            "amount":amount, 
            "totalamount":totalamount
        }
        return render(request, "app/showcart.html",context)
    else:
        return redirect("/cart")
    

@login_required
def minus_cart(request,pk):
    product=Product.objects.get(id=pk)
    c=Cart.objects.get(Q(product=product) & Q(user=request.user))
    if c.quantity==1:
        c.delete()
    else:
        c.quantity-=1
        c.save()
    

    carts=Cart.objects.filter(user=request.user)
    
    amount=0.0
    shipping_amount=50.0
    totalamount=0.0
    cart_product=[]
    for p in carts:
        cart_product.append(p)

    
    if cart_product:
        for p in cart_product:
            temp_amount=(p.quantity * p.product.discounted_price)
            amount+=temp_amount
        totalamount=amount+shipping_amount
        context={
            "carts":carts,
            "quantity":c.quantity,
            "amount":amount, 
            "totalamount":totalamount
        }
        return render(request,"app/showcart.html",context)
    else:
        return redirect("/cart")
    

@login_required
def remove_cart(request,pk):
    
    product=Product.objects.get(id=pk)
    c=Cart.objects.get(Q(product=product) & Q(user=request.user))
    
    c.delete()

    carts=Cart.objects.filter(user=request.user)
    amount=0.0
    shipping_amount=50.0
    totalamount=0.0
    cart_product=[]
    for p in carts:
        cart_product.append(p)
    if cart_product:
        for p in cart_product:
            temp_amount=(p.quantity * p.product.discounted_price)
            amount+=temp_amount
        totalamount=amount+shipping_amount
        context={
            "carts":carts,
            "amount":amount, 
            "totalamount":totalamount
        }
        return render(request, "app/showcart.html",context)
    else:
        return redirect("/cart")
    

def search(request):
    keyword=request.GET["keyword"]
    print(keyword)
    search_results=Product.objects.filter(Q(description__icontains=keyword)| Q(title__icontains=keyword))
    return render(request, "app/search.html",{"search_results":search_results,"keyword":keyword})
    
@login_required
def buy(request):
    return render(request, "app/buynow.html")

# def profile(request):
#     return render(request, "app/profile.html")
class ProfileView(View):

    def get(self,request):
        form=MyCustomerForm()
        return render(request, "app/profile.html",{"form":form,"active":"btn-primary"})

    def post(self,request):
        form=MyCustomerForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data["name"]
            locality=form.cleaned_data["locality"]
            city=form.cleaned_data["city"]
            state=form.cleaned_data["state"]
            zipcode=form.cleaned_data["zipcode"]
            phone_number=form.cleaned_data["phone_number"]
            reg=Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode, phone_number=phone_number)
            reg.save()

        return render(request, "app/profile.html",{"form":form,"active":"btn-primary"})


@login_required
def address(request):
    address=Customer.objects.filter(user=request.user)
    return render(request, "app/address.html",{"address":address,"active":"btn-primary"})

@login_required
def orders(request):
    return render(request, "app/orders.html")

@login_required
def password_change(request):
    return render(request, "app/password_change.html")

def mobile(request, data=None):
    if data==None:
        mobiles=Product.objects.filter(category="M")

    elif (data=="Oppo" or data=="Samsung" or data=="Motorola"):
        mobiles=Product.objects.filter(category="M").filter(brand__iexact=data)

    elif data=="below":
        mobiles=Product.objects.filter(category="M").filter(discounted_price__lt=20000)
    
    elif data=="above":
        mobiles=Product.objects.filter(category="M").filter(discounted_price__gt=20000)

    return render(request, "app/mobile.html",{"mobiles":mobiles})

def laptop(request, data=None):
    if data==None:
        laptops=Product.objects.filter(category="L")

    elif (data=="Acer" or data=="Lenovo" ):
        laptops=Product.objects.filter(category="L").filter(brand__iexact=data)

    elif data=="below":
        laptops=Product.objects.filter(category="L").filter(discounted_price__lt=50000)
    
    elif data=="above":
        laptops=Product.objects.filter(category="L").filter(discounted_price__gt=50000)

    return render(request, "app/laptop.html",{"laptops":laptops})

def topwear(request, data=None):
    if data==None:
        topwears=Product.objects.filter(category="TW")

    elif (data=="cottonwear" or data=="Nike" ):
        topwears=Product.objects.filter(category="TW").filter(brand__iexact=data)

    elif data=="below":
        topwears=Product.objects.filter(category="TW").filter(discounted_price__lt=1000)
    
    elif data=="above":
        topwears=Product.objects.filter(category="TW").filter(discounted_price__gt=1000)

    return render(request, "app/topwear.html",{"topwears":topwears})


def bottomwear(request, data=None):
    if data==None:
        bottomwears=Product.objects.filter(category="BW")

    elif (data=="levis" or data=="denim" ):
        bottomwears=Product.objects.filter(category="BW").filter(brand__iexact=data)

    elif data=="below":
        bottomwears=Product.objects.filter(category="BW").filter(discounted_price__lt=1500)
    
    elif data=="above":
        bottomwears=Product.objects.filter(category="BW").filter(discounted_price__gt=1500)

    return render(request, "app/bottomwear.html",{"bottomwears":bottomwears})

class MyRegistrationView(View):
    
    def get(self,request):
        form=MyRegistrationForm()
        return render(request, "app/registration.html", {"form":form} )

    def post(self, request):
        form=MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! Registered Successfully.')
        
        return render(request, "app/registration.html", {"form":form})


# def registration(request):
#     return render(request, "app/registration.html") 
@login_required
def checkout(request):
    user= request.user
    address=Customer.objects.filter(user=user)
    if address:
        cart_items=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=50
        cart_product=[]
        for p in cart_items:
            cart_product.append(p)
        
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            totalamount = amount+shipping_amount
        context={"address":address, "cart_items":cart_items,"totalamount":totalamount}
        
        return render(request, 'app/checkout.html',context)
    else:
        messages.warning(request,"Please add Address")
        return redirect("/profile")

@login_required
def payment_done(request):
    custid=request.GET.get('custid')
    print(f"custid :{custid}")
    user=request.user
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product,
        quantity=c.quantity).save()
        c.delete()
    
    return redirect("orders")


@login_required
def orders(request):
	orders = OrderPlaced.objects.filter(user=request.user)
	return render(request, 'app/orders.html', {'orders':orders})