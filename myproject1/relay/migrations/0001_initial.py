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
            name='Relay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ETH_MAC', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('activation', models.CharField(max_length=100)),
                ('input_protocol', models.CharField(max_length=100)),
                ('input_modbus_TCP_client', models.CharField(max_length=100)),
                ('input_alarm_sensor_list', models.CharField(max_length=100)),
                ('input_local_manual', models.CharField(max_length=100)),
                ('output_modbus_TCP_IP_IP', models.CharField(max_length=100)),
                ('output_modbus_TCP_IP_type', models.CharField(max_length=100)),
                ('output_modbus_TCP_IP_address', models.CharField(max_length=100)),
                ('output_modbus_TCP_IP_timeout', models.IntegerField()),
                ('output_modbus_TCP_IP_ID', models.CharField(max_length=100)),
                ('output_modbus_RTU_port', models.CharField(max_length=100)),
                ('output_modbus_RTU_address', models.IntegerField()),
                ('output_modbus_RTU_type', models.CharField(max_length=100)),
                ('output_modbus_RTU_ID', models.IntegerField()),
                ('output_modbus_RTU_timeout', models.IntegerField()),
                ('output_modbus_RTU_parity', models.CharField(max_length=100)),
                ('output_modbus_RTU_stop_bits', models.IntegerField()),
                ('output_modbus_RTU_data_bits', models.IntegerField()),
                ('output_modbus_RTU_baudrate', models.IntegerField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thiet_bi.thietbi')),
            ],
        ),
    ]
