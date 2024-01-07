from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import (
    LoginForm,
)

urlpatterns = [
    path('',views.ProductView.as_view(),name='home'),
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name="product-detail"),
    path('cart/', views.showcart, name='showcart'),
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    path('pluscart/',views.plus_cart,name="pluscart"),
    path("minuscart/",views.minus_cart,name="minuscart"),
    path("removecart/",views.remove_cart,name="removecart"),
    path("registration/",views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('login/', views.login, name='login'),
    path("profile",views.ProfileView.as_view(),name="profile"),
    path("paymentdone/", views.payment_done, name="paymentdone"),
    path('address/', views.address, name='address'),
    path('buy/', views.buy_now, name='buy-now'),
    path('changepassword/', views.change_password, name='changepassword'),    
    path('orders/', views.orders, name='orders'),
    
    path('checkout/', views.checkout, name='checkout'),
    path(
        "account/Login/",
        auth_views.LoginView.as_view(
            template_name="app/login.html", authentication_form=LoginForm
        ),
        name='login',
    )

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
