from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,Product
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import F
from django.db.models import Q
from .forms import ProductForm
from django.urls import reverse


def product(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request,'product/html/product.html',{'categories': categories})


def category_list(request,id):
    category = get_object_or_404(Category,id=id)
    product_list = Product.objects.filter(category__id=id)
    products = category.products.all()
    return render(request,'product/html/category.html',context={'products':products,'product_list':product_list})




def product_detail(request,id):
       
    product = get_object_or_404(Product, id=id)
    Product.objects.filter(id=id).update(view=F('view') + 1)
    product.refresh_from_db()
    
    
    return render(request,'product/html/product_detail.html',context={'detail':product})




@login_required
def add_product_view(request):
    if request.user.user_type != 'vendor':
        messages.error(request, " دسترسی لازم برای افزودن محصول را ندارید.")
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user  
            product.save()
            messages.success(request, " با موفقیت ثبت شد.")
            return redirect('my_products')  
        else:
            print("=== خطاهای اعتبارسنجی فرم ===")
            print(form.errors)
            print("=================================")
    else:
        form = ProductForm()

    return render(request, 'product/html/add_product.html', {'form': form})




@login_required
def my_products_view(request):
   
    if request.user.user_type != 'vendor':
        messages.error(request, "شما دسترسی به این صفحه را ندارید.")
        return redirect('home')

 
    products = Product.objects.filter(vendor=request.user).order_by('-id')

    return render(request, 'product/html/my_products.html', {'products': products})




def live_search_view(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
       
        normalized_query = query.replace('ي', 'ی').replace('ك', 'ک')

        
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(name__icontains=normalized_query) |
            Q(brand__title__icontains=query) |
            Q(brand__title__icontains=normalized_query)
        ).distinct()[:10]

        for item in products:
            results.append({
                'id': item.id,
                'name': item.name,
                'price': f"{item.price:,}" if hasattr(item, 'price') and item.price else "0",
                'image': item.image.url if item.image else '',
               
                'url': reverse('product_detail', args=[item.id]),
            })

    return JsonResponse({'results': results})








@login_required
def edit_product(request, product_id):
    
    product = get_object_or_404(Product, id=product_id, vendor=request.user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات  با موفقیت ذخیره شد.')
            return redirect('my_products')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'product/html/add_product.html', {
        'form': form,
        'is_edit': True,
        'product': product
    })



@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, vendor=request.user)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'محصول با موفقیت حذف شد.')
        
    return redirect('my_products')
















    
    