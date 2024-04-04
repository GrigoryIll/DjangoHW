from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=200)
    reg_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    add_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    total_sum = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
