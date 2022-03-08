# Generated by Django 4.0.3 on 2022-03-08 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('fecha_edicion', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('id', models.AutoField(db_column='dispositivo_id', primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(db_column='nombre_equipo', max_length=100)),
                ('potencia_actual', models.IntegerField(db_column='potencial_actual')),
            ],
            options={
                'db_table': 'dim_dispositivo',
            },
        ),
        migrations.CreateModel(
            name='EstatusDispositivo',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('fecha_edicion', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('id', models.AutoField(db_column='estatus_dispositivo_id', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=200)),
            ],
            options={
                'db_table': 'cat_estatus_dispositivo',
            },
        ),
        migrations.CreateModel(
            name='TipoDispositivo',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('fecha_edicion', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('id', models.AutoField(db_column='tipo_dispositivo_id', primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(db_column='nombre_tipo', max_length=100)),
            ],
            options={
                'db_table': 'cat_tipo_dispositivo',
            },
        ),
        migrations.CreateModel(
            name='Lecturas',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('fecha_edicion', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('id', models.AutoField(db_column='id_lectura', primary_key=True, serialize=False)),
                ('potencia_actual', models.IntegerField(db_column='potencial_actual_id')),
                ('dispositivo', models.ForeignKey(db_column='dispositivo_id', on_delete=django.db.models.deletion.CASCADE, to='app.dispositivo')),
                ('tipo_dispositivo', models.ForeignKey(db_column='tipo_dispositivo_id', on_delete=django.db.models.deletion.PROTECT, to='app.tipodispositivo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='status_dispositivo',
            field=models.ForeignKey(db_column='status_dispositivo_id', on_delete=django.db.models.deletion.PROTECT, to='app.estatusdispositivo'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='tipo_dispositivo',
            field=models.ForeignKey(db_column='tipo_dispositivo_id', on_delete=django.db.models.deletion.PROTECT, to='app.tipodispositivo'),
        ),
    ]
