from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("user_portal/", include("user_portal.urls")),
]
