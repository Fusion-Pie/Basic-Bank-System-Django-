# Generated by Django 4.0.4 on 2022-05-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie_bank_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=200),
        ),
    ]