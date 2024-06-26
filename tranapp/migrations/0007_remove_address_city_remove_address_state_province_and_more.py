# Generated by Django 5.0.4 on 2024-04-22 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranapp', '0006_alter_address_state_province_alter_userinfo_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street_address',
        ),
        migrations.AddField(
            model_name='address',
            name='campus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tranapp.campus', verbose_name='校区'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='用户470700', max_length=128, verbose_name='昵称'),
        ),
    ]
