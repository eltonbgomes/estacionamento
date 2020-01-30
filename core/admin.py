from django.contrib import admin
from .models import (
    Pessoa,
    Marca, 
    Veiculo, 
    Parametros, 
    MovRotativo
)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total')

admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)