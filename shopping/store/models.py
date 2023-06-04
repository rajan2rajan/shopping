from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return  self.title  


class Customer(models.Model):
    user = models.OneToOneField(User,max_length=200,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null = True , blank= True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',max_length=200,default=None)
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warrenty = models.CharField(max_length=100,default="NO")
    return_policy = models.CharField(max_length=200)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return  self.title  
    
    @property
    def discount_rate(self):
        percentage = ((self.marked_price-self.selling_price)/self.marked_price)*100
        decimal_digit = '%.2f'%percentage
        return decimal_digit


class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    total_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  'cart:' +str(self.id)
    


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return "cart: "+str(self.cart.id) + "cart Product "+str(self.id)

ORDER_STATUS = (
    # shown in database ,   shown in form 
    ('Order recived ',"order recived"),
    ('Order processing','order processing'),
    ('On the way','on the way'),
    ('Order completed','order completed'),
    ('Order cancled','order cancled'),

)


class Order(models.Model):
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=100,null=False)
    shipping_address = models.CharField(max_length=100, null= False,blank=False)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(null=False,blank=False)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50,choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        return "order :" +str(self.id)