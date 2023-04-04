from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mim', views.about, name='about'),
    path("servicos", views.services, name="services"),
    path("paginas", views.pages, name="pages"),
    path("contato", views.contact, name="contact")
]
