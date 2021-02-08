from django.contrib import admin

# Register your models here.

from.models import Departamentos,Denuncia,Tipo_ciberdelito,Tipo_incidente,Plataforma,Denuncia


admin.site.register(Denuncia)
admin.site.register(Departamentos)
admin.site.register(Tipo_incidente)
admin.site.register(Tipo_ciberdelito)
admin.site.register(Plataforma)
