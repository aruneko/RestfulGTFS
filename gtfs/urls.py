from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from gtfs import views

router = SimpleRouter()
router.register(r"agencies", views.AgencyViewSet)
router.register(r"stops", views.StopViewSet)
router.register(r"routes", views.RouteViewSet)
router.register(r"services", views.ServiceViewSet)
router.register(r"trips", views.TripViewSet)
router.register(r"offices", views.OfficeViewSet)
router.register(r"fare_attributes", views.FareAttributeViewSet)
router.register(r"shapes", views.ShapeViewSet)
router.register(r"transfers", views.TransferViewSet)
router.register(r"feed_info", views.FeedInfoViewSet)
router.register(r"translations", views.TranslationViewSet)

stop_times_by_stop_router = NestedSimpleRouter(router, r"stops", lookup="stop")
stop_times_by_stop_router.register(
    r"stop_times", views.StopTimeViewSet, base_name="stop_time"
)

stop_times_by_trip_router = NestedSimpleRouter(router, r"trips", lookup="trip")
stop_times_by_trip_router.register(
    r"stop_times", views.StopTimeViewSet, base_name="stop_time"
)

service_date_router = NestedSimpleRouter(router, r"services", lookup="service")
service_date_router.register(
    r"service_dates", views.ServiceDateViewSet, base_name="service_date"
)

trips_by_route_router = NestedSimpleRouter(router, r"routes", lookup="route")
trips_by_route_router.register(r"trips", views.TripViewSet, base_name="trips_by_route")

trips_by_office_router = NestedSimpleRouter(router, r"offices", lookup="office")
trips_by_office_router.register(
    r"trips", views.TripViewSet, base_name="trips_by_office"
)

fare_rules_by_fare_attribute_router = NestedSimpleRouter(
    router, r"fare_attributes", lookup="fare_attribute"
)
fare_rules_by_fare_attribute_router.register(
    r"fare_rules", views.FareRuleViewSet, base_name="fare_rules_by_fare_attribute"
)


urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^", include(stop_times_by_stop_router.urls)),
    url(r"^", include(stop_times_by_trip_router.urls)),
    url(r"^", include(service_date_router.urls)),
    url(r"^", include(trips_by_route_router.urls)),
    url(r"^", include(trips_by_office_router.urls)),
    url(r"^", include(fare_rules_by_fare_attribute_router.urls)),
]
