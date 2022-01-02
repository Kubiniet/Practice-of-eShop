from django.db import models
from django.conf import settings

CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Smartwatch'),
    ('TV','Televisor')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    name = models.CharField(max_length=50)
    price=models.FloatField()
    discount_price=models.FloatField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    labelChoices=models.CharField(max_length=1,choices=LABEL_CHOICES)
    slug = models.SlugField()
    description =models.TextField()
    
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       from django.shortcuts import reverse
       return reverse('core:product', kwargs={'slug': self.slug})

class OrderItems(models.Model):
    items=models.ForeignKey(Item,on_delete=models.CASCADE)
    def __str__(self):
        return self.name    
    


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItems)
    start_date=models.DateTimeField(auto_now_add=True)
    order_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username