from django.urls import path

from factoryboy_lecture.bucket_list import views
from factoryboy_lecture.bucket_list.views.country_views import country_list_view

app_name = "bucket_list"

urlpatterns = [
    path("country/list/", country_list_view, name="country-list"),
]
