# Generated by Django 2.2.24 on 2021-06-16 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('children', 'Children')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protype', models.CharField(blank=True, choices=[('summer', 'Summer'), ('winter', 'Winter')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, choices=[('long', 'Long'), ('medium', 'Medium'), ('short', 'Short'), ('xl', 'xl'), ('xxl', 'xxl')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('prize', models.CharField(help_text='entet price of product', max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.Category')),
                ('product_type', models.ManyToManyField(help_text='select a product type', to='productapp.ProType')),
                ('size', models.ManyToManyField(help_text='select size of the product', to='productapp.Size')),
            ],
        ),
    ]
