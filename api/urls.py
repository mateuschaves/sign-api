from django.urls import path
from .views import get_documents, create_document, handle_webhook, update_document, delete_document, delete_signer, get_companies, get_document

urlpatterns = [
    path('documents/get', get_documents, name='get_documents'),
    path('documents/<int:document_id>', get_document, name='get_document'),
    path('documents/<int:document_id>/patch', update_document, name='update_document'),
    path('documents/<int:document_id>/delete', delete_document, name='delete_document'),
    path('signers/<int:signer_id>/delete', delete_signer, name='delete_signer'),
    path('documents/post', create_document, name='create_document'),
    path('companies', get_companies, name='get_companies'),
    path('webhook/', handle_webhook, name='handle_webhook'),
]
