# -*- coding: utf-8 -*-
from rest_framework import routers

from meta_dados_rio.meta_forms import views

router = routers.DefaultRouter()
router.register(r"tags", views.TagViewSet, basename="tag")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"projects", views.ProjectViewSet, basename="project")
router.register(r"datasets", views.DatasetViewSet, basename="dataset")
router.register(r"tables", views.TableViewSet, basename="table")
router.register(r"columns", views.ColumnViewSet, basename="column")
