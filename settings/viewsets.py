from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListModelViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    A viewset that provides default `list()` actions.
    """

    pass
