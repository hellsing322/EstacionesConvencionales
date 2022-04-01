# Generated by Django 3.2.9 on 2022-03-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRestEstacionesConvencionales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesos',
            fields=[
                ('id_acceso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'accesos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cantones',
            fields=[
                ('id_canton', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField()),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cantones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Captores',
            fields=[
                ('id_captor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'captores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CaptoresTipos',
            fields=[
                ('id_captor_tipo', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'captores_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuencas',
            fields=[
                ('codigo', models.CharField(blank=True, max_length=8, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('id_cuenca', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nivel', models.IntegerField(blank=True, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cuencas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DireccionesViento',
            fields=[
                ('id_dir_viento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('abreviacion', models.CharField(max_length=5)),
                ('grados', models.IntegerField(blank=True, null=True)),
                ('estado', models.BooleanField()),
            ],
            options={
                'db_table': 'direcciones_viento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distritos',
            fields=[
                ('id_distrito', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=600)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'distritos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estaciones',
            fields=[
                ('id_estacion', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('fecha_levantamiento', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('informacion', models.TextField(blank=True, null=True)),
                ('dataloger', models.TextField(blank=True, null=True)),
                ('img_norte', models.BinaryField(blank=True, null=True)),
                ('img_sur', models.BinaryField(blank=True, null=True)),
                ('img_este', models.BinaryField(blank=True, null=True)),
                ('img_oeste', models.BinaryField(blank=True, null=True)),
                ('vista_interna', models.BooleanField(blank=True, null=True)),
                ('vista_externa', models.BooleanField(blank=True, null=True)),
                ('us_ingreso', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_ingreso1', models.DateTimeField(blank=True, null=True)),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'estaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadosEstacion',
            fields=[
                ('id_estado_estacion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('icono', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'estados_estacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FenomenosNaturales',
            fields=[
                ('id_fen_nat', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre', models.CharField(blank=True, max_length=110, null=True)),
                ('icono', models.BinaryField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fenomenos_naturales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneroNubes',
            fields=[
                ('id_genero_nube', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=30, null=True)),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
                ('icono', models.BinaryField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('cifrado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'genero_nubes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetodosAcceso',
            fields=[
                ('id_metodo_acceso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'metodos_acceso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquias',
            fields=[
                ('id_parroquia', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField()),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parroquias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfundidadesGeotemp',
            fields=[
                ('id_profundidad_geotemp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
            ],
            options={
                'db_table': 'profundidades_geotemp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Propietarios',
            fields=[
                ('id_propietario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('representante', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('informe', models.CharField(blank=True, max_length=100, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'propietarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id_provincia', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PuntosObservacion',
            fields=[
                ('id_punto_obs', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('img_norte', models.BinaryField(blank=True, null=True)),
                ('img_sur', models.BinaryField(blank=True, null=True)),
                ('img_este', models.BinaryField(blank=True, null=True)),
                ('img_oeste', models.BinaryField(blank=True, null=True)),
                ('estado', models.BooleanField()),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'puntos_observacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('id_region', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'regiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TEstadosValidacion',
            fields=[
                ('id_estado_validacion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('icono', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'estados_validacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDato',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_dato', models.TextField()),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'tipo_dato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEstaciones',
            fields=[
                ('id_tipo_estacion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField()),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('codigo', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'tipo_estaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoGeotemperaturas',
            fields=[
                ('id_tipo_geotemp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
            ],
            options={
                'db_table': 'tipo_geotemperaturas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposCalculoEvap',
            fields=[
                ('id_tipo_calculo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipos_calculo_evap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadesMedida',
            fields=[
                ('id_unidad_medida', models.IntegerField(primary_key=True, serialize=False)),
                ('simbolo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('us_ingreso', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('us_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'unidades_medida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('contrasenia', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('persona_fk', models.BigIntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=1, null=True)),
                ('conv', models.BooleanField()),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('id_zona', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('us_ingreso', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField()),
                ('us_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zonas',
                'managed': False,
            },
        ),
    ]
