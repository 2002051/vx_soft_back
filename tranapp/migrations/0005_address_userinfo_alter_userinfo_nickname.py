# Generated by Django 5.0.4 on 2024-04-22 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranapp', '0004_alter_book_price_alter_userinfo_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='userinfo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tranapp.userinfo', verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='用户543266', max_length=128, verbose_name='昵称'),
        ),
    ]
