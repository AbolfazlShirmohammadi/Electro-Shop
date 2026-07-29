from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.





class Category(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Product(models.Model):
    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='فروشنده',
        null=True,   
        blank=True
    )


    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    brand = models.ForeignKey(Brand,related_name='products',on_delete=models.CASCADE)
    mojoud = 'موجود'
    namojoud = 'ناموجود'
    mojoudi = [
        (mojoud,'موجود'),
        (namojoud,'ناموجود')
    ]

    mojoudi_label = models.CharField(
        max_length=7,
        choices=mojoudi,
        default=mojoud
    )




    name = models.CharField(max_length=200)
    
    inputV = models.PositiveIntegerField()
    outV = models.PositiveIntegerField()
    wattage = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='products/')
    view = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
         
        super().save(*args, **kwargs)

        
        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

           
            target_size = (800, 800)

            
            if img.height > target_size[1] or img.width > target_size[0]:
               
                img.thumbnail(target_size, Image.Resampling.LANCZOS)
                
                 
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                    
                
                img.save(img_path, quality=85, optimize=True)

    def __str__(self):
        return self.name