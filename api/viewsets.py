from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Avg, Count, Max, Min, \
    F, FloatField, ExpressionWrapper

from api.models import Data
from api import serializers, filters as myfilters


class DataViewset(ReadOnlyModelViewSet):
    # queryset with adding extra calculated field
    queryset = Data.objects.annotate(cpi_val=ExpressionWrapper(
        F('spend') / F('installs'), output_field=FloatField()))
    serializer_class = serializers.DataSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = myfilters.DataFilter

    def get_annotation(self, logic, field):
        return {
            field: logic(field, output_field=FloatField()),
        }

    def get_queryset(self):
        """Handle grouping with dynamic field and logics"""
        selection_fields = self.request.GET.get('selection_fields')
        grouping_fields = self.request.GET.get('grouping_fields')
        if selection_fields is None or grouping_fields is None:
            return self.queryset
        selection_fields = selection_fields.split(',')
        grouping_fields = grouping_fields.split(',')
        queryset = self.queryset.values(*grouping_fields)
        logic_dict = {
            'avg': Avg,
            'sum': Sum,
            'count': Count,
            'max': Max,
            'min': Min
        }
        for selection_field in selection_fields:
            try:
                field, logic = selection_field.split('__')
                logic = logic_dict[logic]
                queryset = queryset.annotate(
                    **self.get_annotation(logic, field))
            except Exception as err:
                print(str(err))
                continue
        return queryset
