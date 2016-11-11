from django.contrib import admin

# Register your models here.
from .models import KirrURL
#Mostrar los campos que quiero en el admin
class KirrURLAdmin(admin.ModelAdmin):
	list_display  = ('url','shortcode','timestamp')		

admin.site.register(KirrURL,KirrURLAdmin)