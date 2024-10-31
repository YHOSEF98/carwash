from django.db import models
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    tipoidentificacion = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    

    class meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Category(models.Model):
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description =  models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)
    preciocompra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    inventoriable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Employee(models.Model):
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    document =models.CharField(max_length=19)
    address = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Client(models.Model):
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Sale(models.Model):
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    placa = models.CharField(max_length=6)
    date_joined = models.DateField()
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de ventas'





