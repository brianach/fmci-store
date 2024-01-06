# Generated by Django 3.2.23 on 2024-01-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tier_1', models.CharField(blank=True, max_length=8, null=True)),
                ('tier_2', models.CharField(blank=True, max_length=8, null=True)),
                ('tier_3', models.CharField(blank=True, max_length=8, null=True)),
                ('tier_4', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Digital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('item_1', models.DecimalField(decimal_places=0, max_digits=10)),
                ('item_2', models.DecimalField(decimal_places=0, max_digits=10)),
                ('item_3', models.DecimalField(decimal_places=0, max_digits=10)),
                ('item_4', models.DecimalField(decimal_places=0, max_digits=10)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.service')),
            ],
            options={
                'verbose_name_plural': 'Digital',
            },
        ),
        migrations.CreateModel(
            name='Compute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('item_1', models.DecimalField(decimal_places=0, max_digits=10)),
                ('item_2', models.DecimalField(decimal_places=0, max_digits=10)),
                ('item_3', models.DecimalField(decimal_places=0, max_digits=10)),
                ('item_4', models.DecimalField(decimal_places=0, max_digits=10)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.service')),
            ],
            options={
                'verbose_name_plural': 'Compute',
            },
        ),
    ]
