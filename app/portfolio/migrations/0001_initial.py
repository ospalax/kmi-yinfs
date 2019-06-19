# Generated by Django 2.2.2 on 2019-06-19 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0, verbose_name='Menu item order')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markup', models.CharField(max_length=2000)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Menu')),
            ],
        ),
    ]
