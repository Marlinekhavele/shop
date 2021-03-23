# Generated by Django 3.1.7 on 2021-03-23 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Product Title')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Size',
                'verbose_name_plural': 'Products Sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='available_sizes',
            field=models.ManyToManyField(to='products.ProductSize', verbose_name='Available Sizes'),
        ),
    ]