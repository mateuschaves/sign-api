from rest_framework import serializers
from .models import Company, Document, Signer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'created_at', 'last_updated_at')

class CreateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'company')

class CreateSignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = ('name', 'email')

class ListSignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = ('id', 'name', 'email', 'status')

class ListDocumentSerializer(serializers.ModelSerializer):
    signers = ListSignerSerializer(many=True, read_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Document
        fields = '__all__'


class UpdateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'status', 'name', 'company')

class UpdateSignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = ('id', 'name', 'email')