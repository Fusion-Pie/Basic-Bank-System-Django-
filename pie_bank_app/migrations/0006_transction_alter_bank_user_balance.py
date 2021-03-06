# Generated by Django 4.0.4 on 2022-05-28 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pie_bank_app', '0005_alter_bank_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transction_from', models.CharField(max_length=10, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pie_bank_app.bank_user'))),
                ('Transction_to', models.CharField(max_length=10, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pie_bank_app.bank_user'))),
                ('Amount', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='bank_user',
            name='Balance',
            field=models.FloatField(null=True),
        ),
    ]
