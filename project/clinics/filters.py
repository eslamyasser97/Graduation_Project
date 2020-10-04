import django_filters
from .models import clinic
class ClinicFilter(django_filters.FilterSet):
    class Meta:
        model = clinic
        fields = ['name', 'type_of_city']