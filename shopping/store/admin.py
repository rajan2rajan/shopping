from django.contrib import admin

from .models import * 

admin.site.register([Category,Cart,Customer])


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['user','full_name','address']
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','category','image','marked_price','selling_price','description', 'warrenty', 'return_policy','view_count']
    

# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['customer','total_amount','created_at']


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['cart','product','rate','quantity','total']
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart','ordered_by','shipping_address','mobile','email','subtotal','discount', 'total', 'order_status','created_at']
    

# @admin.register(Category)
# class CategoryrAdmin(admin.ModelAdmin):
#     list_display = ['title','slug']