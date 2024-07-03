# from django.db import models
# from django.contrib.auth.models import User

# # class post(models.Model):
# #     title = models.CharField(max_length=250)
# #     content = models.TextField()
# #     img_url = models.URLField(null=True)
# #     created_at = models.DateTimeField(auto_now_add=True)

# # #optional

# #     def __str__(self):
# #         return self.title


# class Product(models.Model):
#     productname = models.CharField(max_length=250)
#     content = models.TextField()
#     image = models.ImageField(upload_to='images/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     starting_price = models.DecimalField(max_digits=20, decimal_places=2)
#     closing_time = models.DateField()


#     def __str__(self):
#          return self.title

    
#     class Bid(models.Model):
#         product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bids')
#         bid_price = models.DecimalField(max_digits=10, decimal_places=2)
#         bid_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.product.title} - {self.bid_price}"


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

class Product(models.Model):
    productname = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    starting_price = models.DecimalField(max_digits=20, decimal_places=2)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    closing_time = models.DateField()

    def __str__(self):
        return self.productname

class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bids')
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.productname} - {self.bid_price}"
