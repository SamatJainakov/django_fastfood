from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=20, verbose_name='Email')
    password = models.CharField(max_length=20, verbose_name='Password')

    def __str__(self):
        return f'{self.email} - {self.password}'


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    card_number = models.CharField(max_length=20, verbose_name='Card Number')

    def __str__(self):
        return f'{self.name} - {self.card_number}'


class Worker(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    position = models.CharField(max_length=20, verbose_name='Position')

    def __str__(self):
        return f'{self.name} - {self.position}'


class Ingredient(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    extra_price = models.IntegerField(default=0, verbose_name='Extra Price')

    def __str__(self):
        return f'{self.name} - {self.extra_price}'


class Food(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    start_price = models.IntegerField(default=0, verbose_name='Start Price')

    def __str__(self):
        return f'{self.name} - {self.start_price}'


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Food')
    ingredient = models.ManyToManyField(Ingredient, on_delete=models.CASCADE, blank=True, verbose_name='Ingredient')
    client = models.CharField(max_length=50, verbose_name='Client')
    worker = models.CharField(max_length=50, verbose_name='Worker')
    order_date_time = models.DateTimeField(auto_now_add=True, max_length=20, verbose_name='Order Date Time')

    def total_cost(self):
        ingredient_cost = sum(i.extra_price for i in self.ingredient.all())

        return self.food.start_price + ingredient_cost

    def __str__(self):
        return f'{self.food} - {self.ingredient} - {self.client} - {self.worker} - {self.order_date_time}'

    # order = Order.objects.get(id=1)
    # total_cost = order.total_cost()
