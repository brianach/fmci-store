from django.db import models

# Create your models here.


class Service(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    tier_1 = models.CharField(max_length=8, null=True, blank=True)
    tier_2 = models.CharField(max_length=8, null=True, blank=True)
    tier_3 = models.CharField(max_length=8, null=True, blank=True)
    tier_4 = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class BaseService(models.Model):
    service = models.ForeignKey(
        'Service', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()

    item_1 = models.DecimalField(max_digits=10, decimal_places=0)
    item_2 = models.DecimalField(max_digits=10, decimal_places=0)
    item_3 = models.DecimalField(max_digits=10, decimal_places=0)
    item_4 = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        abstract = True


class Compute(BaseService):
    pass

    class Meta:
        verbose_name_plural = 'Compute'

class Digital(BaseService):
    pass

    class Meta:
        verbose_name_plural = 'Digital'
