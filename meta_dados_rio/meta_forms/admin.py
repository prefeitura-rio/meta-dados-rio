# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from meta_dados_rio.meta_forms.models import (
    Category,
    Column,
    Dataset,
    Project,
    Table,
    Tag,
)


class ColumnInlineAdmin(admin.StackedInline):
    model = Column


class ColumnForm(forms.ModelForm):
    AVAILABLE_TYPES = [
        ("STRING", "STRING"),
        ("INT64", "INT64"),
        ("DATE", "DATE"),
        ("DATETIME", "DATETIME"),
        ("FLOAT64", "FLOAT64"),
        ("ARRAY", "ARRAY"),
        ("BIGNUMERIC", "BIGNUMERIC"),
        ("BOOL", "BOOL"),
        ("BYTES", "BYTES"),
        ("GEOGRAPHY", "GEOGRAPHY"),
        ("INTERVAL", "INTERVAL"),
        ("JSON", "JSON"),
        ("NUMERIC", "NUMERIC"),
        ("STRUCT", "STRUCT"),
        ("TIME", "TIME"),
        ("TIMESTAMP", "TIMESTAMP"),
    ]
    type = forms.ChoiceField(choices=AVAILABLE_TYPES)


class DatasetInlineAdmin(admin.TabularInline):
    model = Dataset


class TableInlineAdmin(admin.StackedInline):
    model = Table
    filter_horizontal = ["tags", "categories"]


class TableForm(forms.ModelForm):
    AVAILABLE_UPDATE_FREQUENCIES = [
        ("Nunca", "Nunca"),
        ("Diário", "Diário"),
        ("Semanal", "Semanal"),
        ("Mensal", "Mensal"),
        ("Anual", "Anual"),
    ]
    update_frequency = forms.ChoiceField(choices=AVAILABLE_UPDATE_FREQUENCIES)


class CategoryAdmin(admin.ModelAdmin):
    pass


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
    form = TableForm


class ColumnAdmin(admin.ModelAdmin):
    form = ColumnForm


admin.site.register(Column, ColumnAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
