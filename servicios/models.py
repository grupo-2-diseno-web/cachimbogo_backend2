# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'articulo'


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        db_table = 'asignatura'


class Dificultad(models.Model):
    id_dificultad = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=10)

    class Meta:
        db_table = 'dificultad'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    correo = models.CharField(
        unique=True, max_length=30, blank=True, null=True)
    monedas = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'usuario'


class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_asignatura = models.ForeignKey(
        Asignatura, models.DO_NOTHING, db_column='id_asignatura')

    class Meta:
        db_table = 'tema'


class Subtema(models.Model):
    id_subtema = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_tema = models.ForeignKey(Tema, models.DO_NOTHING, db_column='id_tema')

    class Meta:
        db_table = 'subtema'


class TipoPregunta(models.Model):
    id_tipopregunta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    class Meta:
        db_table = 'tipo_pregunta'


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    enunciado = models.CharField(max_length=1000)
    clave1 = models.CharField(max_length=200)
    clave2 = models.CharField(max_length=200)
    clave3 = models.CharField(max_length=200)
    clave4 = models.CharField(max_length=200)
    clave5 = models.CharField(max_length=200)
    estado = models.IntegerField(blank=True, null=True)
    id_subtema = models.ForeignKey(
        Subtema, models.DO_NOTHING, db_column='id_subtema')
    id_tipopregunta = models.ForeignKey(
        TipoPregunta, models.DO_NOTHING, db_column='id_tipopregunta')
    id_dificultad = models.ForeignKey(
        Dificultad, models.DO_NOTHING, db_column='id_dificultad')
    correcta_num = models.SmallIntegerField(blank=True, null=True)
    informacion = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        db_table = 'pregunta'


class Respuesta(models.Model):
    id_usuario = models.OneToOneField(
        Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_pregunta = models.ForeignKey(
        Pregunta, models.DO_NOTHING, db_column='id_pregunta')
    acertada = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'respuesta'
        unique_together = (('id_usuario', 'id_pregunta'),)


class UsuarioArticulo(models.Model):
    id_usuario = models.OneToOneField(
        Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_articulo = models.ForeignKey(
        Articulo, models.DO_NOTHING, db_column='id_articulo')

    class Meta:
        db_table = 'usuario_articulo'
        unique_together = (('id_usuario', 'id_articulo'),)


class UsuarioAsignatura(models.Model):
    id_usuario = models.OneToOneField(
        Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_asignatura = models.ForeignKey(
        Asignatura, models.DO_NOTHING, db_column='id_asignatura')
    porcentaje = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'usuario_asignatura'
        unique_together = (('id_usuario', 'id_asignatura'),)


class UsuarioSubtema(models.Model):
    id_usuario = models.OneToOneField(
        Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_subtema = models.ForeignKey(
        Subtema, models.DO_NOTHING, db_column='id_subtema')
    completado = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'usuario_subtema'
        unique_together = (('id_usuario', 'id_subtema'),)


class UsuarioTema(models.Model):
    id_usuario = models.OneToOneField(
        Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_tema = models.ForeignKey(Tema, models.DO_NOTHING, db_column='id_tema')
    porcentaje = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'usuario_tema'
        unique_together = (('id_usuario', 'id_tema'),)
