# Generated by Django 4.2.7 on 2023-12-11 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='InfoRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(max_length=2000)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relecloud.cruise')),
            ],
        ),
        migrations.AddField(
            model_name='cruise',
            name='destinations',
            field=models.ManyToManyField(related_name='destinations', to='relecloud.destination'),
        ),
    ]
