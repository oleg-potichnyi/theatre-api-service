from django.shortcuts import render
# from rest_framework import mixins
# from rest_framework.viewsets import GenericViewSet
#
# from theatre.models import Genre
# from theatre.serializers import (
#     GenreSerializer,
# )
#
#
# class GenreViewSet(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     GenericViewSet,
# ):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)