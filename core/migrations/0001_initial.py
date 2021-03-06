# Generated by Django 2.2.8 on 2021-05-03 14:17

import core.models
import django.contrib.postgres.fields
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=True, verbose_name='Is Live?')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Last Time Modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('number', models.IntegerField(verbose_name='Number')),
            ],
            options={
                'verbose_name': 'Counter',
            },
        ),
        migrations.CreateModel(
            name='FeatureBig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=True, verbose_name='Is Live?')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Last Time Modified')),
                ('feature_title', models.CharField(max_length=60, verbose_name='Name')),
                ('feature_desc', models.CharField(max_length=300, verbose_name='Description')),
                ('image', stdimage.models.StdImageField(upload_to=core.models.refactor_name, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Big Feature',
                'verbose_name_plural': 'Big Features',
            },
        ),
        migrations.CreateModel(
            name='FeatureSmall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=True, verbose_name='Is Live?')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Last Time Modified')),
                ('feature_title', models.CharField(max_length=30, verbose_name='Feature Name')),
                ('feature_desc', models.CharField(max_length=120, verbose_name='Description')),
                ('image', stdimage.models.StdImageField(upload_to=core.models.refactor_name, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Small Feature',
                'verbose_name_plural': 'Small Features',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=True, verbose_name='Is Live?')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Last Time Modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('currency', models.CharField(default='$', max_length=4, verbose_name='Currency')),
                ('service_duration', models.CharField(choices=[('Daily', 'Per day'), ('Weekly', 'Per week'), ('Monthly', 'Per month'), ('Yearly', 'Per year')], max_length=7, verbose_name='Duration')),
                ('benefits', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=list, max_length=40), size=10)),
            ],
            options={
                'verbose_name': 'Pricing',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=True, verbose_name='Is Live?')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Last Time Modified')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('opinion', models.CharField(max_length=300, verbose_name='Opinion')),
                ('image', stdimage.models.StdImageField(upload_to=core.models.refactor_name, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=True, verbose_name='Is Live?')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Last Time Modified')),
                ('process_name', models.CharField(max_length=30, verbose_name='Process')),
                ('process_desc', models.CharField(max_length=50, verbose_name='Description')),
                ('image', stdimage.models.StdImageField(upload_to=core.models.refactor_name, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Work Process',
                'verbose_name_plural': 'Work Processes',
            },
        ),
    ]
