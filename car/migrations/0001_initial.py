# Generated by Django 3.2.7 on 2021-11-18 11:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(max_length=250)),
                ('work_time', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField(default=999999999)),
            ],
        ),
        migrations.CreateModel(
            name='Diller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='odder-image')),
                ('title_1', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('title_2', models.CharField(max_length=100)),
                ('description_1', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='service-images')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hudud', models.CharField(choices=[('Toshkent', 'Toshkent'), ('Toshent Vil', 'Toshent Viloyati'), ('Andijon viloyati', 'Andijon viloyati'), ('Buxoro viloyati', 'Buxoro viloyati'), ('Jizzax viloyati', 'Jizzax viloyati'), ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), ('Navoiy viloyati', 'Navoiy viloyati'), ('Namangan viloyati', 'Namangan viloyati'), ('Samarqand viloyati', 'Samarqand viloyati'), ('Surxondaryo viloyati', 'Surxondaryo viloyati'), ('Sirdaryo viloyati', 'Sirdaryo viloyati'), ('Farg`ona  viloyati', 'Farg`ona  viloyati'), ('Xorazm viloyati', 'Xorazm viloyati'), ('Qoraqalpog`iston Respublikasi', 'Qoraqalpog`iston Respublikasi')], default='Toshent shahar', max_length=29)),
                ('murojat_sababir', models.CharField(max_length=100)),
                ('yil', models.IntegerField(default=2021)),
                ('probeg', models.IntegerField(default=0)),
                ('description', ckeditor.fields.RichTextField()),
                ('ism', models.CharField(max_length=100)),
                ('familiya', models.CharField(max_length=100)),
                ('email', models.EmailField(default='asd@gmail.com', max_length=254)),
                ('nomer', models.CharField(max_length=19)),
                ('diller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.diller')),
                ('modellar', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='moddellar', to='car.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='service-images')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='category', to='car.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='car-images')),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('car_image', models.ImageField(upload_to='car-images')),
                ('title_1', models.CharField(max_length=150)),
                ('short_description', ckeditor.fields.RichTextField()),
                ('image_1', models.ImageField(upload_to='car-images')),
                ('title_2', models.CharField(max_length=150)),
                ('long_description', ckeditor.fields.RichTextField()),
                ('title_3', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='car.categorymodel')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='car.colormodel')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
    ]
