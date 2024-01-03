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
    # termprices = models.TupleField(base_field=models.TupleField(
    #    base_field=models.CharField(max_length=20)))
    termprices = models.JSONField()

    class Meta:
        abstract = True


class Labspace(BaseSpace):
    pass


class Deskspace(BaseSpace):
    pass
