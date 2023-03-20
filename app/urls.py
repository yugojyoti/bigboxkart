from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import MyLoginForm,MyPasswordChangeForm

urlpatterns=[
    path("",views.home,name="home"),
    path("product-detail/<int:pk>/",views.product_detail, name="productdetail"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="showcart"),
    path("pluscart/<int:pk>",views.plus_cart, name="pluscart"),
    path("minuscart/<int:pk>",views.minus_cart,name="minuscart"),
    path("removecart/<int:pk>",views.remove_cart,name="removecart"),
    path("search/", views.search, name="search"),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),

    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),

    path("buy/", views.buy, name="buy"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    
    path("mobile/", views.mobile, name="mobile"),


    path("accounts/login/", auth_views.LoginView.as_view(
        template_name="app/login.html", authentication_form=MyLoginForm), name="login"),

    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    path("passwordchange/",auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html",
    form_class= MyPasswordChangeForm,success_url='/passwordchangedone/'),name="passwordchange"),

    path("passwordchangedone/", auth_views.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"),name="passwordchangedone"),


    path("registration/",views.MyRegistrationView.as_view(), name="registration"),
    path("checkout/", views.checkout, name="checkout"),
    path("paymentdone/",views.payment_done, name="paymentdone"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)