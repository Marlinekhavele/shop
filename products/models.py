import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(_('Product Title'), max_length=255,null=False,blank=False)
    description = models.TextField(_('Product Description'), null=True, blank=True)
    active = models.BooleanField(default=True)
    price = models.DecimalField(_('Product Price'), max_digits=15, decimal_places=2)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
