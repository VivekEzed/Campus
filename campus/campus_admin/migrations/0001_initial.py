# Generated by Django 2.2 on 2019-05-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contactnumber', models.IntegerField()),
                ('college', models.TextField()),
                ('place', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]