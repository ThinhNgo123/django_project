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
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation', models.CharField(max_length=100)),
                ('server_url', models.CharField(max_length=100)),
                ('server_port', models.CharField(max_length=100)),
                ('end_point', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('owner_token', models.CharField(max_length=100)),
                ('wan_port_web_app', models.IntegerField()),
                ('wan_port_database', models.IntegerField()),
                ('wan_port_api', models.IntegerField()),
                ('wan_port_ssh', models.IntegerField()),
                ('wan_port_modbus_tcp_ip', models.IntegerField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thiet_bi.thietbi')),
            ],
        ),
    ]