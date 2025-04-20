import csv

from django.conf import settings

from factoryboy_lecture.bucket_list.models import City
from factoryboy_lecture.bucket_list.models import Country


def run(*args):
    app_folder = settings.APPS_DIR / "bucket_list"
    country_file = app_folder /  "tests" / "fixtures"/ "countries.csv"

    with open(country_file) as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["capital"]:
                print(row["name"], row["iso2"], row["region"], row["capital"])
                country, _ = Country.objects.get_or_create(
                    name=row["name"],
                    code=row["iso2"],
                    region=row["region"],
                )
                City.objects.create(
                    name=row["capital"],
                    country=country,
                )
        print(f"Countries and capitals {City.objects.count()} added successfully.")
