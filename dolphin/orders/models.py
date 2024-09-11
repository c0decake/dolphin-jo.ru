from django.db import models


class Orders(models.Model):
    shop = models.ForeignKey(to='Shop', on_delete=models.PROTECT)
    author = models.ForeignKey(to='accounts.Users', on_delete=models.PROTECT)
    rating = models.IntegerField(null=False, default=100)
    work_date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    price = models.IntegerField(null=False)
    post = models.ForeignKey(to='accounts.Post', on_delete=models.SET_NULL, null=True)
    taxi_to = models.BooleanField(default=False)
    taxi_from = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    drinks = models.BooleanField(default=False)
    toilet = models.BooleanField(default=False)


class Shop(models.Model):
    address = models.CharField(max_length=150, null=False)
    district = models.ForeignKey(to='District', on_delete=models.CASCADE)
    director = models.ForeignKey(to='accounts.Users', on_delete=models.SET_NULL, null=True)


class District(models.Model):
    name = models.CharField(max_length=150, null=False)
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=150, null=False)
