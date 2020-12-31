# Generated by Django 3.1.4 on 2020-12-29 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meditation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meditation_type', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('pub_date', models.DateTimeField(verbose_name='meditation date')),
                ('meditation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meditation_log.user')),
            ],
        ),
    ]
