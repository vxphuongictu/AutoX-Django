from django.contrib.auth import get_user_model
from django.db import models
from users.models import *
# Create your models here.


class comment(models.Model):
    comment_id                      = models.AutoField(primary_key=True)
    prd                             = models.ForeignKey('Product', on_delete=models.CASCADE)
    fullname                        = models.CharField(max_length=100, default='', blank=True)
    email                           = models.CharField(max_length=100, default='', blank=True)
    msg                             = models.CharField(max_length=500, default='', blank=True)
    rating                          = models.FloatField(default=0)
    ip_address                      = models.CharField(max_length=50, blank=True)
    create_time                     = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment_id

    class Meta:
        db_table                    = 'comment'

class history_order(models.Model):
    order_data                      = models.CharField(max_length=1000, default='', blank=True)
    transport_fee                   = models.IntegerField(default=0)
    total_payment                   = models.IntegerField(default=0)
    located                         = models.ForeignKey('users.located', on_delete=models.CASCADE)
    payment_method                  = models.BooleanField(default=0)
    order_time                      = models.DateField(auto_now_add=True)
    order_status                    = models.IntegerField(default=0) # 0: Chua order thanh cong, 1: cho xac nhan, 2: da thanh toan, 3: dang chuan bi hang, 4: dang ship
    invoice_code                    = models.CharField(max_length=500, default='', blank=True)
    user                            = models.ForeignKey('users.MyUser', on_delete=models.CASCADE)

class cart(models.Model):
    cart_id                         = models.AutoField(primary_key=True)
    prd                             = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="cart_prd")
    quantity                        = models.IntegerField(blank=True)
    user_id                         = models.IntegerField(blank=True, default='')
    date_added                      = models.DateField(auto_now_add=True)

    class Meta:
        db_table                    = 'cart'

class Product(models.Model):

    product_id                      = models.AutoField(primary_key=True)
    product_name                    = models.CharField(max_length=500, blank=True)
    product_description             = models.TextField(max_length=5000, blank=True)
    product_price                   = models.CharField(max_length=20, blank=True)
    product_image                   = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
    category                        = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name="on_cat")
    product_create_time             = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        db_table    = "products"

    def __str__(self):
        return self.product_name


class Product_attributes(models.Model):
    attribute_id                    = models.AutoField(primary_key=True)
    attribute_name                  = models.CharField(max_length=200, default='', blank=True, unique=True)

    def __str__(self):
        return self.attribute_name

    class Meta:
        db_table                    = "product_attributes"

class Product_attribute_value(models.Model):
    options_choice = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('password', 'Password'),
        ('date', 'Date')
    )
    attribute                       = models.ForeignKey('Product_attributes', on_delete=models.CASCADE, related_name='attribute_value')
    product                         = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="attributes", default='')
    attribute_options               = models.CharField(max_length=100, choices=options_choice, default='', blank=True)
    attribute_value                 = models.CharField(max_length=200, default='', blank=True)
    post_time                       = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.attribute_value

    class Meta:
        db_table                    = "product_attribute_value"

class GalleryImageProduct(models.Model):
    prd                 = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='gallery')
    prd_image           = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, name="image")

    class Meta:
        db_table        = "product_gallery"

class Categories(models.Model):
    cat_id              = models.AutoField(primary_key=True)
    cat_name            = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        db_table        = "categories"

    def __str__(self):
        return self.cat_name

class Product_wishlist(models.Model):
    prd             = models.ForeignKey('Product', on_delete=models.CASCADE)
    user_id         = models.CharField(max_length=200, blank=True, default='')
    date_added      = models.DateField(auto_now_add=True)

    class Meta:
        db_table    = "product_wishlist"

    def __str__(self):
        return self.prd_id

class Jointablesmodel(models.Model):
    product                 = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="meta_data")
    product_name            = models.CharField(max_length=200, default='', blank=True)
    product_description     = models.CharField(max_length=5000, default='', blank=True)
    product_price           = models.CharField(max_length=20, blank=True)
    product_image           = models.CharField(max_length=5000, default='', blank=True)
    attribute_name          = models.CharField(max_length=200, default='', blank=True)
    attribute_value         = models.CharField(max_length=200, default='', blank=True)
    post_time               = models.DateField(auto_now_add=True)
    cat_id                  = models.CharField(max_length=100, blank=True, unique=True)
    cat_name                = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        db_table            = "join_table_models"
