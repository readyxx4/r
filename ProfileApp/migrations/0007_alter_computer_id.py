# Generated by Django 5.1.6 on 2025-02-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0006_alter_computer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='id',
            field=models.CharField(default='', max_length=3, primary_key=True, serialize=False),
        ),
    ]
