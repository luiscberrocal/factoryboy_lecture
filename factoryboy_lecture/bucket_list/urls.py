from django.urls import path

from factoryboy_lecture.bucket_list import views
from factoryboy_lecture.bucket_list.views.activity_views import (
    activity_list_view,
    activity_create_view,
)
from factoryboy_lecture.bucket_list.views.country_views import country_list_view

app_name = "bucket_list"

urlpatterns = [
    path("country/list/", country_list_view, name="country-list"),
    # Activities
    path("activity/list/", activity_list_view, name="activity-list"),
    path("activity/create/", activity_create_view, name="activity-create"),
]
