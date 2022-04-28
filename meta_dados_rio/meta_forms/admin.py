# -*- coding: utf-8 -*-
from django.contrib import admin

from meta_dados_rio.meta_forms.models import (
    Column,
    Dataset,
    Project,
    Table,
    Tag,
)


class ColumnInlineAdmin(admin.StackedInline):
    model = Column


class DatasetInlineAdmin(admin.TabularInline):
    model = Dataset


class TableInlineAdmin(admin.StackedInline):
    model = Table
    filter_horizontal = ["tags"]


class TagAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    inlines = [DatasetInlineAdmin]
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]


class DatasetAdmin(admin.ModelAdmin):
    inlines = [TableInlineAdmin]
    list_display = [
        "__str__",
        "project",
        "name",
        "title_prefix",
    ]
    ordering = ["name"]
    search_fields = ["name", "project__name"]


class TableAdmin(admin.ModelAdmin):
    readonly_fields = ["tags"]
    inlines = [ColumnInlineAdmin]
    list_display = [
        "__str__",
        "dataset",
        "name",
        "title",
        "short_description",
    ]
    ordering = ["name"]
    search_fields = [
        "name",
        "title",
        "short_description",
        "data_owner",
        "publisher_name",
        "publisher_email",
    ]


class ColumnAdmin(admin.ModelAdmin):
    pass


admin.site.register(Column, ColumnAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Tag, TagAdmin)
