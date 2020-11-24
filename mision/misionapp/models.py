# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulo(models.Model):
    descripcion = models.CharField(max_length=45)
    precio = models.IntegerField()
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'articulo'
        unique_together = (('id', 'categoria'),)


class Asignacion(models.Model):
    articulo = models.ForeignKey(Articulo, models.DO_NOTHING, db_column='Articulo_id')  # Field name made lowercase.
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_id')  # Field name made lowercase.
    usuario_rut = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_rut')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asignacion'
        unique_together = (('id', 'articulo', 'departamento', 'usuario_rut'),)


class Cargo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cargo'
    
    def __str__(self):
        return self.descripcion
   


class Categoria(models.Model):
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.descripcion

class Centro(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'centro'

    def __str__(self):
        return self.descripcion

class Comuna(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
        return self.descripcion
class Departamento(models.Model):
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'departamento'


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    calle_numero = models.CharField(max_length=45)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='Cargo_id')  # Field name made lowercase.
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='Comuna_id')  # Field name made lowercase.
    centro = models.ForeignKey(Centro, models.DO_NOTHING, db_column='Centro_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('rut', 'cargo', 'comuna', 'centro'),)
