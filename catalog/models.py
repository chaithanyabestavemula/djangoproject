from django.db import models

class collection(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class promotions(models.Model):
    description=models.TextField(null=True)
    discoun=models.FloatField()

class product(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.PositiveSmallIntegerField(null=True)
    lastupdated=models.DateTimeField(auto_now_add=True)
    collect=models.ForeignKey(collection,on_delete=models.PROTECT)#one to many
    promotions=models.ManyToManyField(promotions)#many to many
    def __str__(self):
        return self.title
class orders(models.Model):
    pending='p'
    completed='c'
    failed='f'
    order_objects=[
        (pending,'pendind'),
        (completed,'completed'),
        (failed,'failed')

    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=10,choices=order_objects,default=pending)

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField()
    def __str__(self):
        return self.name







# Create your models here.
