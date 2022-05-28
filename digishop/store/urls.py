"""digishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.auth import *
from .views.home import *
from .views.details import *
from .views.checkout import *
from .views.payment import *
from .views.order import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='home'),
    path('about', about),
    path('logout',logout_view,name='logout'),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view(),name='login'),
    path('payment/verify' ,payment_verify,name='payment_verify'),
    
    path('payment/<str:slug>' ,create_payment,name='create_payment'),
    path('product/<str:slug>', product_detail_view),
    path('checkout/<str:slug>' ,checkout,name='checkout'),
    path('orders',OrderListView,name='orders')
]
