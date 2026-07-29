from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from home.models import User


@login_required
def info(request):
        
        
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات با موفقیت ویرایش شد.')
            return redirect('home')

    else:
        form = ProfileForm(instance=request.user)

    return render(
        request,
        'account/html/profile.html',
        {
            'form': form
        }
    )
    




        
        
       
    
    
    