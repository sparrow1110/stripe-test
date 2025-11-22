from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text="Price in cents")

    def __str__(self):
        return self.name

    def get_price_in_dollars(self):
        return f"${self.price / 100:.2f}"

class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id}"

    def get_total_price(self):
        return sum(item.price * orderitem.quantity for item, orderitem in
                  [(oi.item, oi) for oi in self.orderitem_set.all()]) / 100

    def get_absolute_url(self):
        return reverse('order_detail', args=[self.id])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)