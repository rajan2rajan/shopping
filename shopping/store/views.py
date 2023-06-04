from django.shortcuts import render,redirect,HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *


# to show all the data with pagination in the data 
def store(request):
    all_data = Product.objects.all()
    paginator = Paginator(all_data,3)
    page_number = request.GET.get('page')
    servicefinal = paginator.get_page(page_number)
    totalpage = servicefinal.paginator.num_pages
    totalpagelist = [n+1 for n in range(totalpage)]        
    return render(request,'store/store.html',{'result':servicefinal,'lastpage':totalpage,'totalpagelist':totalpagelist  })



# this page is for product detail when use click click view or image 

def product_detail(request,slug):
    result = Product.objects.filter(slug=slug)
    data = Product.objects.all() 
    context = {
        'result':result,
        'data':data
    }
    return render(request,'store/productdetail.html',context) 
    # or  no difference 
    return render(request,'store/productdetail.html',{'result':result,'data':data})



def checkout(request):
    return render(request,'store/checkout.html')


def cartadd(request,pk):
    product_id = Product.objects.get(id=pk)
    # session ma cart id vayare data save vako xa ki nai 
    cart_id_in_session = request.session.get('cart_id',None)
    if cart_id_in_session:
        cart_data = Cart.objects.get(id=cart_id_in_session)
        this_product_in_cart = cart_data.cartproduct_set.filter(product =product_id)
        if this_product_in_cart.exists():
            cartProduct = this_product_in_cart.last()
            cartProduct.quantity +=1
            cartProduct.total += product_id.selling_price
            cartProduct.save()
            cart_data.total_amount += product_id.selling_price
            cart_data.save()
        else:
            cartProduct = CartProduct.objects.create(cart = cart_data, product=product_id, rate = product_id.selling_price,quantity = 1,total = product_id.selling_price)
            cart_data.total_amount += product_id.selling_price
            cart_data.save()
        
    else:
        cart_data = Cart.objects.create(total_amount=0)
        request.session['cart_id'] = cart_data.id
        

    return render(request,'store/cart.html')



from django.db.models import Sum
def cart(request):
    result = CartProduct.objects.all()
    counting = CartProduct.objects.count()
    total_sum = CartProduct.objects.aggregate(total_sum=Sum('total'))['total_sum']
    context = {
        'result':result,
        'counting':counting,
        'total_amount':total_sum
    }
    return render(request,'store/cart.html',context)


def aboutus_page(request):
    return render(request,'store/aboutus.html')

def contactus_page(request):
    return render(request,'store/contactus.html')



