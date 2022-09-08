# Generated by Django 4.0.7 on 2022-08-31 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Maharashtra', 'Maharashtra'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Uttarakhand', 'Uttarakhand'), ('Arunachal Pradesh', 'Arunachal Pradesh')], default='Maharashtra', max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('other', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=25)),
                ('end_date', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=25)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
