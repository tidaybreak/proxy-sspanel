# Generated by Django 3.0 on 2020-02-08 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0031_auto_20200208_0928"),
    ]

    operations = [
        migrations.AddField(
            model_name="vmessnode",
            name="relay_offset_port",
            field=models.IntegerField(blank=True, null=True, verbose_name="中转偏移端口"),
        ),
    ]
