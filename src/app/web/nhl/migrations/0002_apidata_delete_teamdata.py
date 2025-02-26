# Generated by Django 5.1.4 on 2024-12-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=3)),
                ('position', models.CharField(max_length=2)),
                ('games_played', models.IntegerField()),
                ('points', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('shots', models.IntegerField()),
                ('blocked_shots', models.IntegerField()),
                ('toi', models.FloatField(help_text='Average time on ice per game in minutes')),
            ],
        ),
        migrations.DeleteModel(
            name='TeamData',
        ),
    ]
