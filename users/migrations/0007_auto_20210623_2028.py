# Generated by Django 3.1.5 on 2021-06-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210608_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]