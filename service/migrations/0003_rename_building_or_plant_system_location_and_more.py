# Generated by Django 4.0.4 on 2022-10-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_remove_system_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='system',
            old_name='building_or_plant',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='location_in_system',
        ),
        migrations.RemoveField(
            model_name='system',
            name='city',
        ),
        migrations.RemoveField(
            model_name='system',
            name='company',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='documentation',
            field=models.FileField(blank=True, upload_to='documentation/'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='system',
            name='documentation',
            field=models.FileField(blank=True, upload_to='documentation/'),
        ),
    ]
