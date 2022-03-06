from django.db import models
from uuid import uuid4


# Model for the store
class Store(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True)
    added_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


# Model for category
class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    added_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


# Model for the store's products
class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store')
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET("Uncategorized"), related_name='category')
    added_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name
