# Generated by Django 4.2.10 on 2024-03-29 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thiet_bi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('time', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thiet_bi.thietbi')),
            ],
        ),
    ]
