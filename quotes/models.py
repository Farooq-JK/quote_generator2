from django.db import models

# Model for a Quote
class Quote(models.Model):
    client_name = models.CharField(max_length=255)
    client_address = models.TextField()
    project_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_name} - {self.client_name}"

    def total_cost(self):
        """
        Calculate the total cost of all items in this quote.
        """
        return sum(item.total_cost() for item in self.items.all())

# Model for individual items in a Quote
class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subcontractor = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_cost(self):
        """
        Calculate the total cost of this item.
        """
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.item_name} - {self.quantity} x {self.unit_price}"
