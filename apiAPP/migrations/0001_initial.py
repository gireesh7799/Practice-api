# Generated by Django 3.1 on 2020-08-20 13:30

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=120)),
                ('customer_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('survey', models.URLField()),
                ('status', models.CharField(choices=[('allowed', 'allowed'), ('not_allowed', 'not_allowed')], max_length=50)),
                ('c_date', models.DateField(auto_now=True)),
                ('Emp_type', models.CharField(choices=[('project_manager', 'project_manager'), ('leadership', 'leadership'), ('bidder', 'bidder')], max_length=50)),
                ('start_date', models.DateField(default=datetime.date(2020, 8, 20))),
                ('end_date', models.DateField()),
                ('revenue', models.IntegerField()),
                ('cpi', models.FloatField(default=0)),
                ('completes', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('client_contactnumber', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message="Contact number must be in the format of '+123456789'. Up to 13 digits allowed.", regex='^\\+?1?\\d{9,13}$')])),
            ],
        ),
    ]
