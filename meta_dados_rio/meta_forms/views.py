# -*- coding: utf-8 -*-
from typing import List

from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework import permissions

from meta_dados_rio.meta_forms.models import (
    Column,
    Dataset,
    Project,
    Table,
    Tag,
)
from meta_dados_rio.meta_forms.serializers import (
    ColumnSerializer,
    DatasetSerializer,
    ProjectSerializer,
    TableSerializer,
    TagSerializer,
)


def home_view(request):
    return HttpResponseRedirect("/api/")


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Tag.objects.prefetch_related(
            Prefetch(
                "tables",
                Table.objects.prefetch_related(
                    Prefetch("columns", Column.objects.filter(name__isnull=False))
                ),
            )
        ).order_by("name")
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.prefetch_related(
            Prefetch(
                "datasets",
                Dataset.objects.prefetch_related(
                    Prefetch(
                        "tables",
                        Table.objects.prefetch_related(
                            Prefetch(
                                "columns", Column.objects.filter(name__isnull=False)
                            )
                        ),
                    )
                ),
            )
        ).order_by("name")
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class DatasetViewSet(viewsets.ModelViewSet):
    serializer_class = DatasetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Dataset.objects.prefetch_related(
            Prefetch(
                "tables",
                Table.objects.prefetch_related(
                    Prefetch("columns", Column.objects.filter(name__isnull=False))
                ),
            )
        ).order_by("name")
        project_name = self.request.query_params.get("project", None)
        if project_name is not None:
            queryset = queryset.filter(project__name=project_name)
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Table.objects.prefetch_related(
            Prefetch("columns", Column.objects.filter(name__isnull=False))
        ).order_by("name")
        project_name = self.request.query_params.get("project", None)
        if project_name is not None:
            queryset = queryset.filter(dataset__project__name=project_name)
        dataset_name = self.request.query_params.get("dataset", None)
        if dataset_name is not None:
            queryset = queryset.filter(dataset__name=dataset_name)
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ColumnViewSet(viewsets.ModelViewSet):
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Column.objects.all().order_by("id")
        queryset = queryset.filter(name__isnull=False)
        project_name = self.request.query_params.get("project", None)
        if project_name is not None:
            queryset = queryset.filter(table__dataset__project__name=project_name)
        dataset_name = self.request.query_params.get("dataset", None)
        if dataset_name is not None:
            queryset = queryset.filter(table__dataset__name=dataset_name)
        table_name = self.request.query_params.get("table", None)
        if table_name is not None:
            queryset = queryset.filter(table__name=table_name)
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
