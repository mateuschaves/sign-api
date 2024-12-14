from django.db import models

class SignatureStatus(models.TextChoices):
        SIGNED = 'SIGNED', 'signed'
        PENDING = 'PENDING', 'pending'
        NEW = 'NEW', 'new'
        LINK_OPENED = 'LINK_OPENED', 'link_opened'

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    open_id = models.IntegerField(null=False)
    token = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=100, null=False)
    status = models.CharField(
        max_length=15,
        choices=SignatureStatus.choices,
        default=SignatureStatus.PENDING,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    last_updated_at = models.DateTimeField(auto_now=True, null=False)
    created_by = models.EmailField(null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    external_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255, null=False)
    status = models.CharField(
        max_length=15,
        choices=SignatureStatus.choices,
        default=SignatureStatus.NEW,
        null=False
    )
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    external_id = models.CharField(max_length=100, null=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name