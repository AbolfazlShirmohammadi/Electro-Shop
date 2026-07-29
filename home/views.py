from django.shortcuts import render,redirect
from home.forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from product.models import Category

def wellcome(request):
    
    categorys = Category.objects.all()

    return render(request,'home/html/index.html', {'categorys': categorys})



def signup(request):
   
    if request.user.is_authenticated:
        
        return redirect('home')
   
        
    if request.method == 'POST':
         print(request.POST)
         
         form = SignUpForm(request.POST)
        
         if form.is_valid():
             user = form.save() 
       

             messages.success(request, 'حساب کاربری شما با موفقیت ساخته شد. لطفاً وارد شوید.')
             return redirect('login') 
         else:
            
            pass 

    else: 
        form = SignUpForm()

    return render(request, 'home/html/signup.html', {'form': form})



def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)

            messages.success(
                request,
                "با موفقیت وارد حساب کاربری شدید."
            )

            return redirect('home')

        else:
            messages.error(
                request,
                "نام کاربری یا رمز عبور اشتباه است."
            )


    return render(request,'home/html/login.html')
