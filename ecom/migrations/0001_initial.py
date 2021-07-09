# Generated by Django 3.2.4 on 2021-07-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default='')),
                ('desc', models.CharField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=2000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=3000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='ecom/images')),
            ],
        ),
    ]
