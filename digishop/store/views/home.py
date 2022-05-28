from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView,ListView
from store.models import Product,Category
from django.views import View



class HomeView(ListView):
    model= Product
    template_name='store/index.html'
    context_object_name='products'

    def get_context_data(self):
        category_pk=self.request.GET.get("category")
        categories=Category.objects.all()

        if category_pk:
            products = Product.objects.filter(category=category_pk,active=True)

        else:
            products=Product.objects.filter(active=True)

        context={
            'categories' :categories,
            'products' : products,
        }
       
        return context



def about(request):
    return HttpResponse("Hello about")