# -*- coding: utf-8 -*-
# Generated by Django 4.0.4 on 2022-05-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_forms", "0008_alter_table_categories_alter_table_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="table",
            name="categories",
            field=models.ManyToManyField(
                blank=True, related_name="tables", to="meta_forms.category"
            ),
        ),
        migrations.AlterField(
            model_name="table",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tables", to="meta_forms.tag"
            ),
        ),
    ]
