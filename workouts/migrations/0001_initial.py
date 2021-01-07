# Generated by Django 3.1.4 on 2021-01-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('one', models.TextField()),
                ('two', models.TextField()),
                ('three', models.TextField()),
                ('four', models.TextField()),
                ('five', models.TextField()),
                ('six', models.TextField()),
                ('seven', models.TextField()),
                ('eight', models.TextField()),
                ('nine', models.TextField()),
                ('ten', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
