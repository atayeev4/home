# Generated by Django 4.2.9 on 2024-05-06 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='apartment_images')),
                ('description', models.TextField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('metres', models.PositiveSmallIntegerField()),
                ('price', models.PositiveSmallIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='main.city')),
            ],
            options={
                'verbose_name': 'Апартамент',
                'verbose_name_plural': 'Апартаменты',
            },
        ),
    ]
