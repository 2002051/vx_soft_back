# Generated by Django 5.0.4 on 2024-05-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranapp', '0011_alter_banner_options_book_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='咨询')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('image', models.ImageField(upload_to='news/', verbose_name='封面')),
                ('content', models.TextField(verbose_name='详情')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='用户667572', max_length=128, verbose_name='昵称'),
        ),
    ]
