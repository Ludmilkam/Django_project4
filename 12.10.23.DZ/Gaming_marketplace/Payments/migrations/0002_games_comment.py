# Generated by Django 4.2.5 on 2023-10-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
