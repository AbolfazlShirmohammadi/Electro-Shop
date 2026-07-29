from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Usertype(models.TextChoices):
        customer = 'customer','مشتزی'
        vendor = 'vendor','فروشنده'
        


    phone_number = models.CharField(max_length=11,unique=True,verbose_name='شماره تماس')
    address = models.TextField(blank=True,null=True,verbose_name='آدرس')
    user_type = models.CharField(
        max_length=10,
        choices=Usertype.choices,
        default=Usertype.customer,
        verbose_name='نوع کاربر'
    )
    profile_picture = models.ImageField(upload_to='profiles/',blank=True,null=True,verbose_name='تصویر پروفایل')

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'