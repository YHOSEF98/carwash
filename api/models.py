from django.db import models

# Create your models here.
class Empresa(models.Model):
    tipoidentificacion = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Category(models.Model):
    empresa = models.ForeignKey(Empresa)
    name = models.CharField(max_length=50)
    description =  models.CharField(max_length=150)

    class meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Product(models.Model):
    empresa = models.ForeignKey(Empresa)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=150)
    decription = models.CharField(max_length=150)

    class meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class employee(models.Models):
    empresa = models.ForeignKey(Empresa)
    name = models.CharField(max_length=150)
    document =models.CharField(max_length=19)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    
    class meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'







