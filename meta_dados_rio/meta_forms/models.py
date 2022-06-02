# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    path = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    title_prefix = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="datasets"
    )

    def __str__(self):
        return f"{self.project}.{self.name}"

    def __repr__(self):
        return self.__str__()

    def clean(self) -> None:
        # Check if there's a dataset with same name under the same project
        if self.pk is None:
            if Dataset.objects.filter(name=self.name, project=self.project).exists():
                raise ValidationError(
                    f'Já existe um dataset com nome "{self.name}" no projeto "{self.project}"'
                )
        return super().clean()

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ) -> None:
        # Check if there's a dataset with same name under the same project
        if self.pk is None:
            if Dataset.objects.filter(name=self.name, project=self.project).exists():
                raise ValidationError(
                    f'Já existe um dataset com nome "{self.name}" no projeto "{self.project}"'
                )
        return super().save(force_insert, force_update, using, update_fields)


class Table(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    update_frequency = models.CharField(max_length=100)
    temporal_coverage = models.CharField(max_length=100)
    data_owner = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    publisher_email = models.EmailField()
    source_database = models.CharField(max_length=100)
    source_table = models.CharField(max_length=100)
    source_query = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="tables", blank=True)
    categories = models.ManyToManyField(Category, related_name="tables", blank=True)
    dataset = models.ForeignKey(
        Dataset, on_delete=models.CASCADE, related_name="tables"
    )

    def __str__(self):
        return f"{self.dataset}.{self.name}"

    def __repr__(self):
        return self.__str__()

    def clean(self) -> None:
        # Check if there's a table with same name under the same dataset
        if self.pk is None:
            if Table.objects.filter(name=self.name, dataset=self.dataset).exists():
                raise ValidationError(
                    f'Já existe uma tabela com nome "{self.name}" no dataset "{self.dataset}"'
                )
        return super().clean()

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ) -> None:
        # Check if there's a table with same name under the same dataset
        if self.pk is None:
            if Table.objects.filter(name=self.name, dataset=self.dataset).exists():
                raise ValidationError(
                    f'Já existe uma tabela com nome "{self.name}" no dataset "{self.dataset}"'
                )
        return super().save(force_insert, force_update, using, update_fields)


class Column(models.Model):
    original_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100)
    description = models.TextField()
    is_sensitive = models.BooleanField(default=True)
    temporal_coverage = models.CharField(max_length=100, null=True, blank=True)
    measurement_unit = models.CharField(max_length=100, null=True, blank=True)
    contains_dict = models.BooleanField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="columns")

    def __str__(self):
        return f"{self.table}.{self.name}"

    def __repr__(self):
        return self.__str__()

    def clean(self) -> None:
        # Check if there's a column with same name under the same table
        if self.pk is None:
            if Column.objects.filter(name=self.name, table=self.table).exists():
                raise ValidationError(
                    f'Já existe uma coluna com nome "{self.name}" na tabela "{self.table}"'
                )
        return super().clean()

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ) -> None:
        # Check if there's a column with same name under the same table
        if self.pk is None:
            if Column.objects.filter(name=self.name, table=self.table).exists():
                raise ValidationError(
                    f'Já existe uma coluna com nome "{self.name}" na tabela "{self.table}"'
                )
        return super().save(force_insert, force_update, using, update_fields)
