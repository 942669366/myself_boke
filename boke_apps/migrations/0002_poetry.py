# Generated by Django 4.0.6 on 2022-07-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boke_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='poetry',
            fields=[
                ('poetrys_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poetrys', models.CharField(max_length=1000)),
            ],
        ),
    ]
