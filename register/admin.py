from models import Company
from models import Product
from models import Compaign
#from models import UrlQRCode
from django.contrib import admin

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Compaign)

#class UrlQRCodeAdmin(admin.ModelAdmin):
#	list_display = ('url', 'qr_code')
#admin.site.register(UrlQRCode, UrlQRCodeAdmin)
