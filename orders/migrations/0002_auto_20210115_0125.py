# Generated by Django 3.1.5 on 2021-01-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20210114_1522'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dish_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='dish_quantity',
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_quantity', models.IntegerField(default=1)),
                ('dish_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.menu')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
        ),
    ]
