from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import City, Apartment, Image, UserApplication, Type


class ImageInline(admin.StackedInline):
    model = Image 
    extra = 1
    max_num = 12

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width=70 height=70>")


class ApartmentInline(admin.StackedInline):
    model = Apartment
    extra = 1


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display: list[str] = ['id', 'title', 'price', 'city']
    ordering = ['id']
    inlines = [ImageInline]

    

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(UserApplication)
class UserApplicationAdmin(admin.ModelAdmin):
    fields = ['name', 'phone_number', 'description']
    readonly_fields = ['name', 'phone_number', 'description']

    @admin.display(description="Phone")
    def phone_number(self, obj):
        return f"+993{obj.phone}"
    

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [ApartmentInline]
    ordering = ['id']

