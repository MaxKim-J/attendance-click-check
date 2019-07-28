# Generated by Django 2.2.3 on 2019-07-27 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend_name', models.CharField(max_length=100)),
                ('status_time', models.DateTimeField(verbose_name='Status Time')),
            ],
        ),
        migrations.CreateModel(
            name='Comers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='Join Time')),
                ('attend_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Status')),
            ],
        ),
    ]