# Generated by Django 3.0.2 on 2020-01-30 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_movrotativo_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo')),
            ],
        ),
    ]
