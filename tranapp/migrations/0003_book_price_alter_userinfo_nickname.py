# Generated by Django 5.0.4 on 2024-04-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranapp', '0002_userinfo_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=1, max_length=5, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='用户793544', max_length=128, verbose_name='昵称'),
        ),
    ]
