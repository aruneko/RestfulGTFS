from jpbusformat.models.agency import Agency
from jpbusformat.models.office import Office
from jpbusformat.models.route import Route
from jpbusformat.models.service import Service
from jpbusformat.models.service_date import ServiceDate
from jpbusformat.models.stop import Stop
from jpbusformat.models.stop_time import StopTime
from jpbusformat.models.trip import Trip
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from gtfs.serializers import (
    AgencySerializer,
    StopSerializer,
    StopTimeSerializer,
    RouteSerializer,
    ServiceSerializer,
    ServiceDateSerializer,
    TripSerializer,
    OfficeSerializer,
)


class AgencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class StopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer


class StopTimeViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = StopTimeSerializer

    def get_queryset(self):
        if self.kwargs.get("stop_pk"):
            return StopTime.objects.filter(stop__id=self.kwargs["stop_pk"]).order_by("departure_time")
        elif self.kwargs.get("trip_pk"):
            return StopTime.objects.filter(trip__id=self.kwargs["trip_pk"]).order_by("sequence")


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDateViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ServiceDateSerializer

    def get_queryset(self):
        return ServiceDate.objects.filter(service_id=self.kwargs["service_pk"])


class TripViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        if self.kwargs.get("route_pk"):
            return Trip.objects.filter(route_id=self.kwargs["route_pk"])
        else:
            return Trip.objects.all()


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def filter_queryset(self, queryset):
        if self.kwargs.get("trip_pk"):
            return queryset.filter(trip__id=self.kwargs["trip_pk"])
        else:
            return queryset
