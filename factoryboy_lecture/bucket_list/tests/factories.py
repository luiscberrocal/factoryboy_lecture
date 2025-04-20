import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText
from django.utils.timezone import now
from bucket_list.models import Country, City, Place, Activity, WishlistItem, DoneItem


class CountryFactory(DjangoModelFactory):
    name = factory.Faker("country")
    code = factory.Faker("country_code")

    class Meta:
        model = Country


class CityFactory(DjangoModelFactory):
    name = factory.Faker("city")
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = City


class PlaceFactory(DjangoModelFactory):
    name = factory.Faker("company")
    city = factory.SubFactory(CityFactory)
    address = factory.Faker("address")
    description = factory.Faker("text")

    class Meta:
        model = Place


class ActivityFactory(DjangoModelFactory):
    name = factory.Faker("word")
    description = factory.Faker("text")

    class Meta:
        model = Activity


class WishlistItemFactory(DjangoModelFactory):
    place = factory.SubFactory(PlaceFactory)
    activity = factory.SubFactory(ActivityFactory)
    notes = factory.Faker("text")
    added_date = factory.LazyFunction(now)
    priority = FuzzyInteger(1, 5)

    class Meta:
        model = WishlistItem


class DoneItemFactory(DjangoModelFactory):
    place = factory.SubFactory(PlaceFactory)
    activity = factory.SubFactory(ActivityFactory)
    completion_date = factory.LazyFunction(now)
    notes = factory.Faker("text")
    rating = FuzzyInteger(1, 5)

    class Meta:
        model = DoneItem
