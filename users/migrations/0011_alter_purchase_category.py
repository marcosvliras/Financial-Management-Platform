# Generated by Django 4.2.5 on 2023-09-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_purchase_credit_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='category',
            field=models.CharField(choices=[('Education', 'Education'), ('Health', 'Health'), ('Travel', 'Travel'), ('Electronics', 'Electronics'), ('Investment', 'Investment'), ('Clothing', 'Clothing'), ('Food', 'Food'), ('Entertainment', 'Entertainment'), ('HOME', 'Home')], default=None, max_length=20),
        ),
    ]
