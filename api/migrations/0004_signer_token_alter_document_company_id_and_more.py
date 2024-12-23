# Generated by Django 5.1 on 2024-12-14 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_signer_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='signer',
            name='token',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='company_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AlterField(
            model_name='document',
            name='created_by',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='document',
            name='external_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('SIGNED', 'Signed'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], default='PENDING', max_length=15),
        ),
        migrations.AlterField(
            model_name='signer',
            name='document_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.document'),
        ),
        migrations.AlterField(
            model_name='signer',
            name='external_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signer',
            name='status',
            field=models.CharField(choices=[('SIGNED', 'Signed'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], default='PENDING', max_length=15),
        ),
    ]
