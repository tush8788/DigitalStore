from django.shortcuts import redirect, render
from store.models import Product
from store.models import UserProduct
from store.models import Payment
from store.forms import CheckoutForm
from django.views.decorators.csrf import csrf_exempt
from math import floor
import razorpay

client = razorpay.Client(auth=("rzp_test_sMcBqHO39k7TlA", "QCcTgUWKm36PRAfA4ltf308Q"))

@csrf_exempt
def payment_verify(request):
    if request.method=='POST':
        print(request.POST)
        razorpay_payment_id=request.POST['razorpay_payment_id']
        razorpay_order_id=request.POST['razorpay_order_id']
        razorpay_signature=request.POST['razorpay_signature']

        payment=Payment.objects.get(order_id=razorpay_order_id)
        payment.status="SUCCESS"
        payment.payment_id=razorpay_payment_id
        payment.save()
        # print("Order id by tushar : "+ razorpay_signature)
        user_product=UserProduct(user=payment.user, payment=payment,product=payment.product)
        user_product.save()

        return render(request,template_name='store/payment_success.html')
        
def create_payment(request,slug):
        template_name=''
        form=CheckoutForm(request.POST)
        context={}
        product=Product.objects.get(slug=slug)
        user=None
        if request.user.is_authenticated:
            user=request.user
            
        else:
            return redirect('login')


        if form.is_valid():
            print("payment")
            template_name='store/checkout.html'

            price=floor((product.price-(product.price*product.discount*0.01)))
            order_amount=price*100
            print(order_amount)
            email=form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
    # Creating order razerpay       
            

            DATA = {
                "amount": order_amount,
                "currency": "INR",
                "receipt": "receipt#1",
                "notes": {
                    "email": email,
                    "phone": phone,
                    
                }
            }
            order=client.order.create(data=DATA)
            # Create payment
            payment=Payment(product=product, user=user,status='FAIL',order_id=order.get('id'))
            payment.save()

            context={
                'user':user,
                'product':product,
                'order':order,
                'show_payment_dialog': True,
                'form' : form,
            }
        else:
            context={
                'product' :product,
                'form' : form,
            }
            template_name='store/checkout.html'
        return render(request, template_name=template_name,context=context)