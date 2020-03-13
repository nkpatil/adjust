from django_filters import rest_framework as filters

from api.models import Data

COMPARE_FILTERS = ['lte', 'gte', 'lt', 'gt', 'exact']
MATCH_FILTERS = ['exact', 'in']


class DataFilter(filters.FilterSet):
    class Meta:
        model = Data
        fields = {
            'date': COMPARE_FILTERS,
            'channel': MATCH_FILTERS,
            'country': MATCH_FILTERS,
            'os': MATCH_FILTERS
        }
