from django.db import models

# Create your models here.
class Spaces(models.Model):

    class Meta:
        verbose_name_plural = 'Spaces'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Labspace(models.Model):
    labspace = models.ForeignKey('Labspace', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    space_category = models.TextField()
    term = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Deskspace(models.Model):
    deskspace = models.ForeignKey('Deskspace', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    space_category = models.TextField()
    term = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name