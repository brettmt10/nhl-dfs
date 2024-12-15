# Generated by Django 5.1.4 on 2024-12-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhl', '0002_apidata_delete_teamdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='DkData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.CharField(blank=True, max_length=10, null=True)),
                ('ppg', models.FloatField(blank=True, help_text='Points per game', null=True)),
            ],
        ),
    ]