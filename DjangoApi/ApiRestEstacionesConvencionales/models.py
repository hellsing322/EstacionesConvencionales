# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   class Meta Rearrange models' order
#   class Meta Make sure each model has one field with primary_key=True
#   class Meta Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   class Meta Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class T1073161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1073161h'


class T1073161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1073161h_val'


class T1123161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1123161h'


class T1123161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1123161h_val'


class T1263011D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1263011d'


class T1263011M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1263011m'


class T1263021D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1263021d'


class T1263021M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1263021m'


class T1263041D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1263041d'


class T1263041M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1263041m'


class T12827161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_12827161d'


class T12827161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    id_genero_nube = models.IntegerField()
    octas = models.IntegerField(blank=True, null=True)
    altura_suelo = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_12827161h'


class T12827161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    id_genero_nube = models.IntegerField()
    octas = models.IntegerField(blank=True, null=True)
    altura_suelo = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_12827161h_val'


class T12827161M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_12827161m'


class T13028161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_13028161d'


class T13028161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_13028161h'


class T13028161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_13028161h_val'


class T13028161M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_13028161m'


class T141011D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_141011d'


class T141011M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_141011m'


class T1410161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1410161h'


class T1410161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1410161h_val'


class T141021D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_141021d'


class T141021M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_141021m'


class T141041D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_141041d'


class T141041M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_141041m'


class T1714161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    suma = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1714161d'


class T1714161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1714161h'


class T1714161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    suma = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_1714161h_val'


class T171481D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_171481d'


class T171481H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_171481h'


class T171481HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_171481h_val'


class T171481M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_171481m'


class T187161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    pres_atmf_prom = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_corregida_prom = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_convertida_prom = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_reducida_prom = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_microbarografo_prom = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_187161d'


class T187161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    pres_atmof = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_corregida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_convertida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_reducida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_microbarografo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_187161h'


class T187161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    pres_atmof = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_corregida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_convertida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_reducida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pres_microbarografo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_187161h_val'


class T261111D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_261111d'


class T261111M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_261111m'


class T272981D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_272981d'


class T272981H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_272981h'


class T272981HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_272981h_val'


class T272981M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_272981m'


class T293161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    id_estacion = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    maximo = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    minimo = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    promedio = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_293161d'


class T293161M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    id_estacion = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    maximo = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    minimo = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    promedio = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_293161m'


class T29321M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_29321m'


class T3211D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_3211d'


class T3211M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_3211m'


class T323161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_323161h'


class T323161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_323161h_val'


class T32321D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_32321d'


class T32321M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    valor = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    anual = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_32321m'


class T3711161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    id_estacion = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    id_dir_viento = models.IntegerField()
    velocidad_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    velocidad_min = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    velocidad_prom = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    recorrido_viento = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_3711161d'


class T3711161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    id_estacion = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    id_dir_viento = models.IntegerField()
    velocidad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    recorrido_viento = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_3711161h'


class T3711161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    id_estacion = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    id_dir_viento = models.IntegerField()
    velocidad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    recorrido_viento = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_3711161h_val'


class T42161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_42161h'


class T42161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_42161h_val'


class T573161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_573161h'


class T573161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_573161h_val'


class T583161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_583161h'


class T583161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_583161h_val'


class T597161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_597161h'


class T597161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_597161h_val'


class T603161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_603161h'


class T603161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_603161h_val'


class T613161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_613161h'


class T613161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_613161h_val'


class T614161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    id_tipo_calculo_evap = models.IntegerField()
    lect_micrometro = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    reduc_tanque = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    agua_sacada = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    agua_aniadida = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    evaporacion = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_614161h'


class T614161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    id_tipo_calculo_evap = models.IntegerField()
    lect_micrometro = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    reduc_tanque = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    agua_sacada = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    agua_aniadida = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    evaporacion = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_614161h_val'


class T621161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_621161h'


class T621161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_621161h_val'


class T644161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_644161h'


class T644161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_644161h_val'


class T7127161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField()
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7127161d'


class T7127161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField()
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7127161h'


class T7127161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField()
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7127161h_val'


class T7127161M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField()
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7127161m'


class T7229161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7229161h'


class T7229161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_7229161h_val'


class T734161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_734161h'


class T734161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_734161h_val'


class T775161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_775161d'


class T91161D(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    maximo = models.IntegerField(blank=True, null=True)
    minimo = models.IntegerField(blank=True, null=True)
    promedio = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_91161d'


class T91161H(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_91161h'


class T91161HVal(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    validado = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_91161h_val'


class T91161M(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    id_estacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    maximo = models.IntegerField(blank=True, null=True)
    minimo = models.IntegerField(blank=True, null=True)
    promedio = models.IntegerField(blank=True, null=True)
    diario = models.BooleanField(blank=True, null=True)
    tipo_dato = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_91161m'


class Accesos(models.Model):
    id_acceso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accesos'


class Cantones(models.Model):
    id_canton = models.CharField(primary_key=True, max_length=4)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia')
    id_distrito = models.ForeignKey('Distritos', models.DO_NOTHING, db_column='id_distrito', blank=True, null=True)
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantones'


class Captores(models.Model):
    id_captor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'captores'


class CaptoresTipos(models.Model):
    id_captor_tipo = models.IntegerField(primary_key=True)
    id_captor = models.ForeignKey(Captores, models.DO_NOTHING, db_column='id_captor')
    id_tipo_estacion = models.ForeignKey('TipoEstaciones', models.DO_NOTHING, db_column='id_tipo_estacion')

    class Meta:
        managed = False
        db_table = 'captores_tipos'
        unique_together = (('id_captor_tipo', 'id_captor', 'id_tipo_estacion'),)


class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Cuencas(models.Model):
    codigo = models.CharField(max_length=8, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    id_cuenca = models.CharField(primary_key=True, max_length=5)
    nivel = models.IntegerField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuencas'


class DireccionesViento(models.Model):
    id_dir_viento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    abreviacion = models.CharField(max_length=5)
    grados = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'direcciones_viento'


class Distritos(models.Model):
    id_distrito = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=600)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distritos'


class Estaciones(models.Model):
    id_estacion = models.IntegerField(primary_key=True)
    id_estado_estacion = models.ForeignKey('EstadosEstacion', models.DO_NOTHING, db_column='id_estado_estacion')
    id_propietario = models.ForeignKey('Propietarios', models.DO_NOTHING, db_column='id_propietario')
    id_punto_obs = models.ForeignKey('PuntosObservacion', models.DO_NOTHING, db_column='id_punto_obs')
    id_captor_tipo = models.ForeignKey(CaptoresTipos, models.DO_NOTHING, db_column='id_captor_tipo')
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_levantamiento = models.DateField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    informacion = models.TextField(blank=True, null=True)
    dataloger = models.TextField(blank=True, null=True)
    img_norte = models.BinaryField(blank=True, null=True)
    img_sur = models.BinaryField(blank=True, null=True)
    img_este = models.BinaryField(blank=True, null=True)
    img_oeste = models.BinaryField(blank=True, null=True)
    vista_interna = models.BooleanField(blank=True, null=True)
    vista_externa = models.BooleanField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso1 = models.DateTimeField(blank=True, null=True)
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estaciones'
        unique_together = (('id_punto_obs', 'id_captor_tipo'),)


class EstadosEstacion(models.Model):
    id_estado_estacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_estacion'


class TEstadosValidacion(models.Model):
    id_estado_validacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_validacion'


class FenomenosNaturales(models.Model):
    id_fen_nat = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=110, blank=True, null=True)
    icono = models.BinaryField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fenomenos_naturales'


class GeneroNubes(models.Model):
    id_genero_nube = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    icono = models.BinaryField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    cifrado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero_nubes'


class MetodosAcceso(models.Model):
    id_metodo_acceso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'metodos_acceso'


class Parroquias(models.Model):
    id_parroquia = models.CharField(primary_key=True, max_length=6)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton')
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquias'


class ProfundidadesGeotemp(models.Model):
    id_profundidad_geotemp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'profundidades_geotemp'


class Propietarios(models.Model):
    id_propietario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    representante = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    informe = models.CharField(max_length=100, blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietarios'


class Provincias(models.Model):
    id_provincia = models.CharField(primary_key=True, max_length=4)
    id_region = models.ForeignKey('Regiones', models.DO_NOTHING, db_column='id_region')
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona')
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias'


class PuntosObservacion(models.Model):
    id_punto_obs = models.IntegerField(primary_key=True)
    id_cuenca = models.ForeignKey(Cuencas, models.DO_NOTHING, db_column='id_cuenca')
    id_parroquia = models.ForeignKey(Parroquias, models.DO_NOTHING, db_column='id_parroquia')
    id_acceso = models.ForeignKey(Accesos, models.DO_NOTHING, db_column='id_acceso')
    id_metodo_acceso = models.ForeignKey(MetodosAcceso, models.DO_NOTHING, db_column='id_metodo_acceso')
    codigo = models.CharField(unique=True, max_length=8)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    img_norte = models.BinaryField(blank=True, null=True)
    img_sur = models.BinaryField(blank=True, null=True)
    img_este = models.BinaryField(blank=True, null=True)
    img_oeste = models.BinaryField(blank=True, null=True)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puntos_observacion'


class Regiones(models.Model):
    id_region = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regiones'


class TipoDato(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo_dato = models.TextField()  # This field type is a guess.
    descripcion = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tipo_dato'


class TipoEstaciones(models.Model):
    id_tipo_estacion = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
    nombre = models.CharField(max_length=50)
    observacion = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    codigo = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_estaciones'


class TipoGeotemperaturas(models.Model):
    id_tipo_geotemp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tipo_geotemperaturas'


class TiposCalculoEvap(models.Model):
    id_tipo_calculo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipos_calculo_evap'


class UnidadesMedida(models.Model):
    id_unidad_medida = models.IntegerField(primary_key=True)
    simbolo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    us_ingreso = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    us_modificacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades_medida'


class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasenia = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    persona_fk = models.BigIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    conv = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuarios'


class Zonas(models.Model):
    id_zona = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas'
