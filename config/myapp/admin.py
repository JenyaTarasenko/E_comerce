from django.contrib import admin

from .models import Product



# в хэдер выводит надпись'Django apps'
admin.site.site_header = 'Django apps'

# в хэдер выводит title
admin.site.site_title = "Django best framewark"

# в хэдер выводит 'My admin'
admin. site.index_title = 'My admin'



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)# поиск по имени в admin
    actions = 'make_zero'#метод
    list_editable = ('price', 'description')


    def make_zero(self, request, queryset):
        """
         метод обнуляет цену в админке
        """
        queryset.update(price=0)



admin.site.register(Product, ProductAdmin)




