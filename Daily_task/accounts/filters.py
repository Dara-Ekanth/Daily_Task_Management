import django_filters
from django_filters import DateFilter, CharFilter, DateTimeFilter
from .models import *

class taskfilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains')
    title = CharFilter(field_name='title',lookup_expr='icontains')
    deadline = DateTimeFilter(field_name='deadline',input_formats=['%d/%m/%Y %H:%M'],lookup_expr='lte')
    date_created = DateTimeFilter(field_name='date_created', input_formats=['%d/%m/%Y %H:%M'], lookup_expr='gte')
    class Meta:
        model = tasks
        fields="__all__"