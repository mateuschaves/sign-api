from django.urls import path
from .views import get_documents, create_document, handle_webhook

urlpatterns = [
    path('documents/<int:company_id>/', get_documents, name='get_documents'),
    path('documents/', create_document, name='create_document'),
    path('webhook/', handle_webhook, name='handle_webhook'),
]
