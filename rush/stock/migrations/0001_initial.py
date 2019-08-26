# Generated by Django 2.2.3 on 2019-07-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('ticker', models.CharField(max_length=10)),
                ('currentprice', models.FloatField()),
                ('increase', models.FloatField()),
                ('lastprice', models.FloatField()),
            ],
        ),
    ]
