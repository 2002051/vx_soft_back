# Generated by Django 5.0.4 on 2024-04-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranapp', '0009_alter_order_status_alter_userinfo_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='banner/', verbose_name='轮播图')),
                ('link', models.CharField(max_length=500, verbose_name='链接')),
                ('remark', models.TextField(verbose_name='备注信息')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='用户850866', max_length=128, verbose_name='昵称'),
        ),
    ]