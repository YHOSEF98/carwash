from django.db import models

# Create your models here.
class Empresa(models.Model):
    tipoidentificacion = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Category(models.Model):
    empresa = models.ForeignKey(Empresa)
    name = models.CharField(max_length=50)
    description =  models.CharField(max_length=150, blank=True, null=True)

    class meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    empresa = models.ForeignKey(Empresa)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)

    class meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Employee(models.Model):
    empresa = models.ForeignKey(Empresa)
    name = models.CharField(max_length=150)
    document =models.CharField(max_length=19)
    address = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    class meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Client(models.Model):
    empresa = models.ForeignKey(Empresa)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)

    class meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Sale(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    placa = models.CharField(max_length=6)
    date_joined = models.DateField()
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    class meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    class meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de ventas'





