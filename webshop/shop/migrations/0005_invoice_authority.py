# Generated by Django 5.0.7 on 2024-09-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_orderitem_product_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='authority',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
