from django.views.generic import ListView

from factoryboy_lecture.bucket_list.models import Country


class CountryListView(ListView):
    model = Country
    template_name = 'bucket_list/country/country_list.html'
    context_object_name = 'countries'
    paginate_by = 10

    def get_queryset(self):
        return Country.objects.all().order_by('name')

country_list_view = CountryListView.as_view()
