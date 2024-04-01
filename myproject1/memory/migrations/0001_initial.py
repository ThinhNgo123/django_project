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
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disk_status', models.CharField(max_length=100)),
                ('disk_name', models.CharField(max_length=100)),
                ('disk_total', models.CharField(max_length=100)),
                ('disk_used', models.CharField(max_length=100)),
                ('disk_free', models.CharField(max_length=100)),
                ('USB1_free', models.CharField(max_length=100)),
                ('USB1_used', models.CharField(max_length=100)),
                ('USB1_total', models.CharField(max_length=100)),
                ('USB1_name', models.CharField(max_length=100)),
                ('USB1_status', models.CharField(max_length=100)),
                ('USB2_free', models.CharField(max_length=100)),
                ('USB2_used', models.CharField(max_length=100)),
                ('USB2_total', models.CharField(max_length=100)),
                ('USB2_name', models.CharField(max_length=100)),
                ('USB2_status', models.CharField(max_length=100)),
                ('USB3_free', models.CharField(max_length=100)),
                ('USB3_used', models.CharField(max_length=100)),
                ('USB3_total', models.CharField(max_length=100)),
                ('USB3_name', models.CharField(max_length=100)),
                ('USB3_status', models.CharField(max_length=100)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thiet_bi.thietbi')),
            ],
        ),
    ]
