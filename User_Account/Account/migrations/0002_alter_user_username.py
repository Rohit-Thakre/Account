# Generated by Django 4.2.6 on 2023-11-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
