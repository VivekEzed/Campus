# Generated by Django 2.2 on 2019-05-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='login',
            name='secondname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
