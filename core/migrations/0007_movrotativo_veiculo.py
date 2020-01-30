# Generated by Django 3.0.2 on 2020-01-30 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_movrotativo_veiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movrotativo',
            name='veiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
            preserve_default=False,
        ),
    ]