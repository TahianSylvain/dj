# Generated by Django 3.2.4 on 2023-12-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesadmin',
            name='adminupload',
            field=models.FileField(upload_to=''),
        ),
    ]
