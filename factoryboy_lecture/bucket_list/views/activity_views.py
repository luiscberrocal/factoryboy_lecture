from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from factoryboy_lecture.bucket_list.forms import ActivityForm
from factoryboy_lecture.bucket_list.models import Activity

class ActivityListView(ListView):
    model = Activity
    template_name = 'bucket_list/activity/activity_list.html'
    context_object_name = 'activities'
    paginate_by = 10

    def get_queryset(self):
        return Activity.objects.all().order_by('name')

activity_list_view = ActivityListView.as_view()

class CreateActivityView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'bucket_list/activity/activity_form.html'
    success_url = reverse_lazy('bucket_list:activity-list')

activity_create_view = CreateActivityView.as_view()
