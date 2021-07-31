from django.urls import path
from .views import acme_webhook

urlpatterns = [
    path('webhook/', acme_webhook, name='webhook'),
]
