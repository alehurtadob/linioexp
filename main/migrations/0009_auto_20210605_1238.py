# Generated by Django 3.2 on 2021-06-05 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210527_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='direccionEntrega',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fechaEntrega',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_entrega',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='repartidor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colaborador'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pedido'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.producto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tarifa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
