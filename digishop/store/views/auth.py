from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import FormView
from django.views.generic.base import View
from django.shortcuts import redirect, render,HttpResponse
# Create your views here.

class SignupView(FormView):
    form_class=UserCreationForm
    template_name='store/signup.html'
    success_url='/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(View):
    def get(self,request):
        form=AuthenticationForm()
        context={
            'form' : form
        }
        return render(request,template_name='store/login.html',context=context)
    
    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('home')
        else:
            context={
            'form' : form
        }
        return render(request,template_name='store/login.html',context=context)
            
def logout_view(request):
    print("logout view")
    request.session.clear()
    return redirect('login')