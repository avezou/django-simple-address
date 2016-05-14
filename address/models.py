from django.db import models
from localflavor.us.models import USStateField
from localflavor.us.models import PhoneNumberField
from django.utils.translation import ugettext as _


class Address(models.Model):
    """
    Address model. This uses the US local flavor for the state field and
    phone numbers
    The customer_name is an optional attribute to keep track of the customer
    at this address without using a foreign key.
    """
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128,
                                 blank=True)
    city = models.CharField(_("city"), max_length=64)
    state = USStateField(_("state"), blank=True)
    zip_code = models.CharField(max_length=10)
    phone_number = PhoneNumberField()
    customer_name = models.CharField(max_length=128, blank=True,
                                     help_text='Customer\'s last name')

    def __str__(self):
        return "%s's address\n @ %s" % (self.customer_name, self.address_1)

    class Meta:
        verbose_name_plural = 'Addresses'
