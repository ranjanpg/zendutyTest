# Generated by Django 5.0.1 on 2024-01-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_reservation_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='finesAccrued',
            field=models.IntegerField(default=0),
        ),
    ]
