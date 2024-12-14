from rest_framework import serializers
from .models import Company, Document, Signer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')

class CreateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'company')

class ListDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'open_id', 'token', 'name', 'status', 'created_at', 'last_updated_at', 'created_by', 'company', 'external_id')

class CreateSignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = ('name', 'email')