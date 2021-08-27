import django_filters
from .models import Tour

class Filters(django_filters.FilterSet):
    class Meta:
        model = Tour
        fields = {
            'title': ['icontains'],
        }