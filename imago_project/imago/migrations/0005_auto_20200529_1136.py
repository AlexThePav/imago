# Generated by Django 3.0.6 on 2020-05-29 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('imago', '0004_member_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='play',
            name='cover',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Photo'),
        ),
    ]
