# Generated by Django 4.2.7 on 2024-01-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(max_length=15, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='car_pics/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
            ],
        ),
    ]