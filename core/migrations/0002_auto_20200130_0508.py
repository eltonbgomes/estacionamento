# Generated by Django 3.0.2 on 2020-01-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
