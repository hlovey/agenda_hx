from django.contrib import admin

from contacts.models import Person, Phone, Address


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('person', 'description', 'phone_number')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('person', 'description', 'address')


admin.site.register(Person, PersonAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Address, AddressAdmin)
