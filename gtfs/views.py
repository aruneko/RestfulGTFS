from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from jpbusformat.models.agency import Agency
from jpbusformat.models.fare_attribute import FareAttribute
from jpbusformat.models.fare_rule import FareRule
from jpbusformat.models.feed_info import FeedInfo
from jpbusformat.models.office import Office
from jpbusformat.models.route import Route
from jpbusformat.models.service import Service
from jpbusformat.models.service_date import ServiceDate
from jpbusformat.models.shape import Shape
from jpbusformat.models.stop import Stop
from jpbusformat.models.stop_time import StopTime
from jpbusformat.models.transfer import Transfer
from jpbusformat.models.translation import Translation
from jpbusformat.models.trip import Trip
from rest_framework import viewsets

from gtfs.serializers import (
    AgencySerializer,
    StopSerializer,
    StopTimeSerializer,
    RouteSerializer,
    ServiceSerializer,
    ServiceDateSerializer,
    TripSerializer,
    OfficeSerializer,
    FareAttributeSerializer,
    FareRuleSerializer,
    ShapeSerializer,
    TransferSerializer,
    FeedInfoSerializer,
    TranslationSerializer,
)
from settings.viewsets import ListModelViewSet


# define GET parameters for documentation
fields_param = openapi.Parameter(
    "fields",
    openapi.IN_QUERY,
    description="抽出したいフィールドをカンマ区切りで記述",
    type=openapi.TYPE_STRING,
)


# define view sets
@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class AgencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    法人番号に該当する事業者を返します

    list:
    登録されている事業者の一覧を返します
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class StopViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する停留所を返します

    list:
    停留所の一覧を返します
    """

    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    search_fields = ("name", "location_type")


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class StopTimeViewSet(ListModelViewSet):
    """
    list:
    通過時刻情報の一覧を返します
    """

    serializer_class = StopTimeSerializer

    def get_queryset(self):
        if self.kwargs.get("stop_pk"):
            return StopTime.objects.filter(stop__id=self.kwargs["stop_pk"]).order_by(
                "departure_time"
            )
        elif self.kwargs.get("trip_pk"):
            return StopTime.objects.filter(trip__id=self.kwargs["trip_pk"]).order_by(
                "sequence"
            )


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する経路を返します

    list:
    経路の一覧を返します
    """

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する運行区分を返します

    list:
    運行区分の一覧を返します
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class ServiceDateViewSet(ListModelViewSet):
    """
    list:
    運行日情報の一覧を返します
    """
    serializer_class = ServiceDateSerializer

    def get_queryset(self):
        return ServiceDate.objects.filter(service_id=self.kwargs["service_pk"])


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class TripViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する便情報を返します

    list:
    便情報の一覧を返します
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        if self.kwargs.get("route_pk"):
            return Trip.objects.filter(route_id=self.kwargs["route_pk"])
        else:
            return Trip.objects.all()


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する営業所を返します

    list:
    営業所の一覧を返します
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def filter_queryset(self, queryset):
        if self.kwargs.get("trip_pk"):
            return queryset.filter(trip__id=self.kwargs["trip_pk"])
        else:
            return queryset


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class FareAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する運賃属性を返します

    list:
    運賃属性の一覧を返します
    """
    queryset = FareAttribute.objects.all()
    serializer_class = FareAttributeSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class FareRuleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する運賃定義を返します

    list:
    運賃定義の一覧を返します
    """
    queryset = FareRule.objects.all()
    serializer_class = FareRuleSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class ShapeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    IDに該当する描画情報を返します

    list:
    描画情報の一覧を返します
    """
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class TransferViewSet(ListModelViewSet):
    """
    list:
    乗り換え情報の一覧を返します
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    search_fields = ("from_stop", "to_stop")


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class FeedInfoViewSet(ListModelViewSet):
    """
    list:
    提供情報の一覧を返します
    """
    queryset = FeedInfo.objects.all()
    serializer_class = FeedInfoSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[fields_param])
)
class TranslationViewSet(ListModelViewSet):
    """
    list:
    翻訳情報の一覧を返します
    """
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    search_fields = ("trans_id", "lang")
