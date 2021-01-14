# Generated by Django 3.1.5 on 2021-01-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=1500, null=True)),
                ('contact', models.IntegerField(null=True)),
                ('orders', models.IntegerField(default=0)),
            ],
        ),
    ]
