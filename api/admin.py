from django.contrib import admin

from api.models import Company, Document, Signer

# Register your models here.
admin.site.register(Company)
admin.site.register(Document)
admin.site.register(Signer)
