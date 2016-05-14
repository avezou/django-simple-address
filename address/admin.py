from django.contrib import admin
from .forms import ZipAdminForm
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    """
    Addres admin page. This uses ZipAdminForm for the address
    form. Currently designed for US addresses only. For non US
    states just ignore the State.
    """
    form = ZipAdminForm
    list_display = ('state', 'city', 'address_1',)
    list_filter = ('city', 'state', 'zip_code',)
    search_fields = ('address_1', 'city', 'state', 'zip_code')

    def get_changelist_form(self, request, **kwargs):
        return ZipAdminForm

admin.site.register(Address, AddressAdmin)
