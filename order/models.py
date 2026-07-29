from django.db import models
from django.conf import settings
from product.models import Product


class Order(models.Model):

    STATUS = (
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت شده'),
        ('sending', 'در حال ارسال'),
        ('delivered', 'تحویل داده شده'),
        ('cancel', 'لغو شده'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='pending'
    )
    
    authority = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    ref_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Order #{self.id}"





class OrderItem(models.Model):
    
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.PositiveIntegerField()

    def total(self):
        return self.quantity * self.price


