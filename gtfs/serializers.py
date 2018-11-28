from drf_dynamic_fields import DynamicFieldsMixin
from jpbusformat.models.agency import Agency
from jpbusformat.models.fare_attribute import FareAttribute
from jpbusformat.models.fare_rule import FareRule
from jpbusformat.models.feed_info import FeedInfo
from jpbusformat.models.frequency import Frequency
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
from jpbusformat.models.zone import Zone
from rest_framework import serializers


class AgencySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    official_name = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="事業者正式名称",
        source="agency.official_name",
    )
    zip_number = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="事業者郵便番号",
        source="agency.zip_number",
    )
    address = serializers.CharField(
        allow_blank=True, allow_null=True, help_text="事業者住所", source="agency.address"
    )
    president_pos = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="代表者肩書",
        source="agency.president_pos",
    )
    president_name = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="代表者氏名",
        source="agency.president_name",
    )

    class Meta:
        model = Agency
        fields = (
            "id",
            "name",
            "url",
            "timezone",
            "lang",
            "phone",
            "fare_url",
            "email",
            "official_name",
            "zip_number",
            "address",
            "president_pos",
            "president_name",
        )


class ZoneSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ("id",)


class StopSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    zone = ZoneSerializer()

    class Meta:
        model = Stop
        fields = (
            "id",
            "code",
            "name",
            "desc",
            "point",
            "zone",
            "url",
            "location_type",
            "parent_station",
            "timezone",
            "wheelchair_boarding",
        )


class RouteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    update_date = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="ダイヤ改正日",
        source="route.update_date")
    origin_stop = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="起点",
        source="route.origin_stop")
    via_stop = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="経由地",
        source="route.via_stop")
    destination_stop = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        help_text="終点",
        source="route.destination_stop")

    class Meta:
        model = Route
        fields = (
            "id",
            "agency_id",
            "short_name",
            "long_name",
            "desc",
            "type",
            "url",
            "color",
            "text_color",
            "sort_order",
            "parent_route_id",
            "update_date",
            "origin_stop",
            "via_stop",
            "destination_stop",
        )


class ServiceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServiceDateSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ServiceDate
        fields = "__all__"


class ShapeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = "__all__"


class OfficeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class FrequencySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = "__all__"


class TripSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    frequency = FrequencySerializer(read_only=True)

    class Meta:
        model = Trip
        fields = (
            "id",
            "route",
            "service",
            "headsign",
            "short_name",
            "direction_id",
            "block_id",
            "shape",
            "wheelchair_accessible",
            "bikes_allowed",
            "desc",
            "desc_symbol",
            "office",
            "frequency",
        )


class StopTimeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = StopTime
        exclude = ("id",)


class FareAttributeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = FareAttribute
        fields = "__all__"


class FareRuleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = FareRule
        fields = "__all__"


class TransferSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class FeedInfoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = FeedInfo
        fields = "__all__"


class TranslationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = "__all__"
