from django.db import models

# Create your models here.


class Space(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    term_a = models.CharField(max_length=8, null=True, blank=True)
    term_b = models.CharField(max_length=8, null=True, blank=True)
    term_c = models.CharField(max_length=8, null=True, blank=True)
    term_d = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class BaseSpace(models.Model):
    space = models.ForeignKey(
        'Space', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()

    price_a = models.DecimalField(max_digits=10, decimal_places=2)
    price_b = models.DecimalField(max_digits=10, decimal_places=2)
    price_c = models.DecimalField(max_digits=10, decimal_places=2)
    price_d = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class Labspace(BaseSpace):
    pass


class Deskspace(BaseSpace):
    pass
