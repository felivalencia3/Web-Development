# Generated by Django 2.0.3 on 2018-10-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageName', models.CharField(max_length=100)),
                ('Url', models.CharField(max_length=100)),
            ],
        ),
    ]
