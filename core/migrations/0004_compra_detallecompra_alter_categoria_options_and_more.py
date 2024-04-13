# Generated by Django 5.0.3 on 2024-04-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('compra_id', models.IntegerField(primary_key=True, serialize=False)),
                ('estado_compra', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_compra',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'managed': False},
        ),
    ]
