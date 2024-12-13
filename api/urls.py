from django.urls import path
from .views import CompanyList, DocumentList, SignerList, CompanyDetail, DocumentDetail, SignerDetail

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company-list'),
    path('documents/', DocumentList.as_view(), name='document-list'),
    path('signers/', SignerList.as_view(), name='signer-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('documents/<int:pk>/', DocumentDetail.as_view(), name='document-detail'),
    path('signers/<int:pk>/', SignerDetail.as_view(), name='signer-detail'),
]
