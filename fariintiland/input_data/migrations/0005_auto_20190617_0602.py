# Generated by Django 2.2 on 2019-06-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0004_auto_20190615_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualanmodel',
            name='tahun_transaksi',
            field=models.IntegerField(default=2010),
        ),
    ]