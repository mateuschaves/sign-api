from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    openId = models.IntegerField()
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    external_id = models.CharField(max_length=100)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
