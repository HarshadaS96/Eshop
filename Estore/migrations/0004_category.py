# Generated by Django 4.0.5 on 2022-06-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0003_product_description_product_image_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
