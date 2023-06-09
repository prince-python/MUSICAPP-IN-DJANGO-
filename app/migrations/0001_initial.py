# Generated by Django 3.2.18 on 2023-04-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='image')),
                ('audio', models.FileField(upload_to='audio')),
                ('duration', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
