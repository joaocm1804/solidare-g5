# Generated by Django 5.2 on 2025-04-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apadrinhamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]
