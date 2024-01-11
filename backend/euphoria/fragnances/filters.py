import django_filters
from .models import Fragnance

class FragnanceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    brand = django_filters.CharFilter(lookup_expr='icontains', label='Бренд')

    class Meta:
        model = Fragnance
        fields = [
            'title', 'brand', 'price',
            'type', 'sex', 'size', 'available', 'rating'
        ]