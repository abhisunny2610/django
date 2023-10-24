from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.admin_dashboard, name="admin_dashboard")
]
