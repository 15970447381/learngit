# Generated by Django 3.0.8 on 2020-07-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200719_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='comment',
            field=models.CharField(default='', max_length=256, verbose_name='评论'),
        ),
    ]