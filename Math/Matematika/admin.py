from django.contrib import admin
from .models import Korisnik
# Register your models here.
class KorisnikAdmin(admin.ModelAdmin):
    def firstName(self, Profile):
        return Profile.user_name.firstName

    def lastName(self, Profile):
        return Profile.user_name.lastName

    list_display = (
        'firstName',
        'lastName'
    )
admin.site.register(Korisnik,KorisnikAdmin)