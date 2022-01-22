from django.urls import re_path

from .views import FactView, RuleView

app_name = "main"

urlpatterns = [
    re_path(r'^facts/$', FactView.as_view(), name='facts'),
    re_path(r'^rules/$', RuleView.as_view(), name='rules'),
]