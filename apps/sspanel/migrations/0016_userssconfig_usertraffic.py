# Generated by Django 2.2.1 on 2019-06-01 07:24

import apps.utils
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0015_auto_20190601_1013")]

    operations = [
        migrations.CreateModel(
            name="UserSSConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(db_index=True, unique=True)),
                ("port", models.IntegerField(default=1025, unique=True)),
                (
                    "password",
                    models.CharField(
                        default=apps.utils.get_short_random_string, max_length=32
                    ),
                ),
                ("enable", models.BooleanField(default=True)),
                ("speed_limit", models.IntegerField(default=0)),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("aes-256-cfb", "aes-256-cfb"),
                            ("aes-128-ctr", "aes-128-ctr"),
                            ("rc4-md5", "rc4-md5"),
                            ("salsa20", "salsa20"),
                            ("chacha20", "chacha20"),
                            ("none", "none"),
                        ],
                        default="aes-128-ctr",
                        max_length=32,
                    ),
                ),
            ],
            options={"verbose_name_plural": "用户SS配置"},
        ),
        migrations.CreateModel(
            name="UserTraffic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(db_index=True, unique=True)),
                (
                    "upload_traffic",
                    models.BigIntegerField(default=0, verbose_name="上传流量"),
                ),
                (
                    "download_traffic",
                    models.BigIntegerField(default=0, verbose_name="下载流量"),
                ),
                (
                    "total_traffic",
                    models.BigIntegerField(default=5368709120, verbose_name="总流量"),
                ),
                (
                    "last_use_time",
                    models.DateTimeField(
                        db_index=True,
                        default=datetime.datetime(1996, 2, 2, 0, 0, 0),
                        verbose_name="上次使用时间",
                    ),
                ),
                (
                    "change_time",
                    models.DateTimeField(
                        db_index=True,
                        default=datetime.datetime(1996, 2, 2, 0, 0, 0),
                        verbose_name="更新时间",
                    ),
                ),
            ],
            options={"verbose_name_plural": "用户流量"},
        ),
    ]
