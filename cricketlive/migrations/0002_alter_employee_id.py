# Generated by Django 4.2.7 on 2024-01-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketlive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]