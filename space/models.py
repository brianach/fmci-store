from django.db import models

# Create your models here.


class Space(models.Model):

    class Meta:
        verbose_name_plural = 'Spaces'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

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

    for letter in ['a', 'b', 'c', 'd']:
        field_name = f'price_{letter}'
        locals()[field_name] = models.DecimalField(
            max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class Labspace(BaseSpace):
    pass


class Deskspace(BaseSpace):
    pass
