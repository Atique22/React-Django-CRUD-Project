# Generated by Django 4.1.6 on 2023-02-13 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_teachers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teachers',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='studEmail',
            new_name='studentEmail',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='studName',
            new_name='studentName',
        ),
    ]
