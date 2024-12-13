from django.shortcuts import render
from rest_framework import generics
from .models import Company, Document, Signer
from .serializers import CompanySerializer, DocumentSerializer, SignerSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SignerList(generics.ListCreateAPIView):
    queryset = Signer.objects.all()
    serializer_class = SignerSerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SignerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Signer.objects.all()
    serializer_class = SignerSerializer


