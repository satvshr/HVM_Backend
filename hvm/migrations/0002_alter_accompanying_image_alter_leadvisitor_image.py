# Generated by Django 4.2.6 on 2023-10-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hvm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accompanying',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='leadvisitor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
