# -*- coding: utf-8 -*-
from rest_framework import serializers

from meta_dados_rio.meta_forms.models import (
    Column,
    Dataset,
    Project,
    Table,
    Tag,
)


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    table = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="table-detail"
    )

    class Meta:
        model = Column
        fields = ["url", "name", "description", "table"]


class TableSerializer(serializers.HyperlinkedModelSerializer):
    dataset = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="dataset-detail"
    )
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = [
            "url",
            "name",
            "title",
            "short_description",
            "long_description",
            "update_frequency",
            "temporal_coverage",
            "data_owner",
            "publisher_name",
            "publisher_email",
            "tags",
            "dataset",
            "columns",
        ]


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="project-detail"
    )
    tables = TableSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = ["url", "name", "title_prefix", "project", "tables"]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    datasets = DatasetSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["url", "name", "datasets"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    tables = TableSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ["url", "name", "tables"]
