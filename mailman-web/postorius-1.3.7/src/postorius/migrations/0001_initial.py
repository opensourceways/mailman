# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressConfirmationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('activation_key', models.CharField(max_length=40)),
                ('created', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                           on_delete=models.CASCADE)),
            ],
        ),
    ]
