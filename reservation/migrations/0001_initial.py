# Generated by Django 4.1.3 on 2022-11-26 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('price', models.FloatField(default=120)),
                ('seats_available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=384)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.train')),
            ],
        ),
    ]
