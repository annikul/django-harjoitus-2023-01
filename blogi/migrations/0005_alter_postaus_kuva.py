# Generated by Django 4.1.6 on 2023-03-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0004_alter_postaus_kuva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postaus',
            name='kuva',
            field=models.ImageField(blank=True, null=True, upload_to='blogi/kuvat'),
        ),
    ]
