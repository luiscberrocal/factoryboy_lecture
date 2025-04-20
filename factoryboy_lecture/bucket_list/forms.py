from django import forms
from factoryboy_lecture.bucket_list.models import Place, Activity

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'city', 'address', 'description', 'owner']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description', 'owner']
