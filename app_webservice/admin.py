from django.contrib import admin
from app_webservice import models
# Register your models here.

admin.site.site_header = 'Administrador de BBDD de Music Pro'
admin.site.site_title = 'Administrador de BBDD de Music Pro'
admin.site.index_title = 'Bienvenido al administrador de BBDD de Music Pro'

admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.Stock)
admin.site.register(models.Movement)
