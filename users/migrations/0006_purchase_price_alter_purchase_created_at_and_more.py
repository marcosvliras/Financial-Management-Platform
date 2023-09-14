# Generated by Django 4.2.5 on 2023-09-14 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_purchase_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='data_of_purchase',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='day_to_receive_the_analysis',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]