# Generated by Django 4.2.1 on 2023-06-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCorrea', '0003_pedido_basico_remove_pedido_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_basico',
            name='fecha_pedido',
            field=models.DateField(),
        ),
    ]
