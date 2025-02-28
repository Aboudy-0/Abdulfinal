# Generated by Django 5.1.6 on 2025-02-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
