from django.db import models

# Create your models here.


class TimestampedModel(models.Model):
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, editable=False, db_column="fecha_creacion"
    )
    fecha_edicion = models.DateTimeField(
        auto_now=True, editable=False, db_column="fecha_edicion"
    )

    class Meta:
        abstract = True


class TipoDispositivo(TimestampedModel):
    id = models.AutoField(primary_key=True, db_column='tipo_dispositivo_id')
    nombre_tipo = models.CharField(max_length=100, db_column='nombre_tipo')

    class Meta:
        db_table = 'cat_tipo_dispositivo'


class EstatusDispositivo(TimestampedModel):
    id = models.AutoField(primary_key=True, db_column='estatus_dispositivo_id')
    descripcion = models.CharField(max_length=200, db_column='descripcion')

    class Meta:
        db_table = 'cat_estatus_dispositivo'


class Dispositivo(TimestampedModel):
    id = models.AutoField(primary_key=True, db_column='dispositivo_id')
    nombre_equipo = models.CharField(max_length=100, db_column='nombre_equipo')
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, models.PROTECT, db_column='tipo_dispositivo_id')
    potencia_actual = models.IntegerField(db_column='potencial_actual')
    status_dispositivo = models.ForeignKey(EstatusDispositivo, models.PROTECT, db_column='status_dispositivo_id')

    class Meta:
        db_table = 'dim_dispositivo'


class Lecturas(TimestampedModel):
    id = models.AutoField(primary_key=True, db_column='id_lectura')
    dispositivo = models.ForeignKey(Dispositivo, models.CASCADE, db_column='dispositivo_id')
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, models.PROTECT, db_column='tipo_dispositivo_id')
    potencia_actual = models.IntegerField(db_column='potencial_actual_id')
