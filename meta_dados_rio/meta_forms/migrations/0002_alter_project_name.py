# -*- coding: utf-8 -*-
# Generated by Django 4.0.4 on 2022-04-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_forms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
