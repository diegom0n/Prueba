# Generated by Django 4.0.5 on 2022-06-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_categoria_rename_activo_marca_activomarca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.TextField()),
                ('precioProducto', models.TextField()),
                ('precioCosto', models.TextField()),
                ('stockProducto', models.TextField()),
                ('descripcionProducto', models.TextField(max_length=100)),
                ('categoriaProducto', models.TextField()),
                ('marcaProducto', models.TextField()),
            ],
        ),
    ]