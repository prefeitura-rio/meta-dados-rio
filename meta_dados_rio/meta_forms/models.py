# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Project(models.Model):
    name = models.CharField(max_length=100)

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


class Table(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField(blank=True)
    update_frequency = models.CharField(max_length=100)
    temporal_coverage = models.CharField(max_length=100)
    data_owner = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    publisher_email = models.EmailField(blank=True)
    source_database = models.CharField(max_length=100)
    source_table = models.CharField(max_length=100)
    source_query = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="tables")
    dataset = models.ForeignKey(
        Dataset, on_delete=models.CASCADE, related_name="tables"
    )

    def __str__(self):
        return f"{self.dataset}.{self.name}"

    def __repr__(self):
        return self.__str__()
