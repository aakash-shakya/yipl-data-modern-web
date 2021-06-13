# Generated by Django 3.2.4 on 2021-06-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('sale', models.IntegerField()),
                ('country', models.CharField(max_length=15, null=True)),
                ('product', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ('year',),
            },
        ),
    ]
