# Generated by Django 3.0.8 on 2020-07-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200720_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='url',
            field=models.CharField(max_length=256, verbose_name='活动链接'),
        ),
    ]
