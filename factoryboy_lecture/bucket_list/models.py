from django.db import models
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2, unique=True, blank=True, null=True, help_text="ISO 3166-1 alpha-2 code")
    region = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        verbose_name_plural = "Cities"
        unique_together = ('name', 'country')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.country.name}"

class Place(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='places', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True, help_text="Optional street address")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        location_str = f" ({self.city})" if self.city else ""
        return f"{self.name}{location_str}"

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class WishlistItem(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='wishlist_items', blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='wishlist_items', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    added_date = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(default=3, help_text="1 = High, 3 = Medium, 5 = Low")

    class Meta:
        verbose_name_plural = "Wishlist Items"

    def __str__(self):
        if self.place and self.activity:
            return f"{self.activity.name} at {self.place.name}"
        elif self.place:
            return f"Visit {self.place.name}"
        elif self.activity:
            return f"Do {self.activity.name}"
        return "Wishlist Item"

class DoneItem(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='done_items', blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='done_items', blank=True, null=True)
    completion_date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])

    class Meta:
        verbose_name_plural = "Done Items"

    def __str__(self):
        if self.place and self.activity:
            return f"Did {self.activity.name} at {self.place.name} on {self.completion_date}"
        elif self.place:
            return f"Visited {self.place.name} on {self.completion_date}"
        elif self.activity:
            return f"Did {self.activity.name} on {self.completion_date}"
        return "Done Item"
