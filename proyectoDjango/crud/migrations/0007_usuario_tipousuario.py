# Generated by Django 4.0.5 on 2022-06-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_tipopago_tipousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
