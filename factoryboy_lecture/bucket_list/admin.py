from django.contrib import admin

from .models import Country, City, Place, Activity, WishlistItem, DoneItem


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    list_filter = ('country',)
    search_fields = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'description')
    list_filter = ('city',)
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'place',
        'activity',
        'notes',
        'added_date',
        'priority',
    )
    list_filter = ('place', 'activity', 'added_date')


@admin.register(DoneItem)
class DoneItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "wishlist_item",
        'completion_date',
        'notes',
        'rating',
    )
    list_filter = ('completion_date',)
