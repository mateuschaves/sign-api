from django.urls import path
from .views import get_documents, create_document

urlpatterns = [
    path('documents/<int:company_id>/', get_documents, name='get_documents'),
    path('documents/', create_document, name='create_document'),
]
