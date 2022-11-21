# -*- coding: utf-8 -*-
from rest_framework import serializers

from meta_dados_rio.meta_forms.models import (
    Category,
    Column,
    Dataset,
    Project,
    Table,
    Tag,
)


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    table = serializers.HyperlinkedRelatedField(
        view_name="table-detail", queryset=Table.objects.all()
    )

    class Meta:
        model = Column
        fields = ["url", "name", "original_name", "description", "type", "table"]


class TableSerializer(serializers.HyperlinkedModelSerializer):
    dataset = serializers.HyperlinkedRelatedField(
        view_name="dataset-detail", queryset=Dataset.objects.all()
    )
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )
    categories = serializers.SlugRelatedField(
        many=True, slug_field="path", queryset=Category.objects.all()
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
            "categories",
            "dataset",
            "columns",
        ]


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField(
        view_name="project-detail", queryset=Project.objects.all()
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


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    tables = TableSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["url", "name", "path", "tables"]
