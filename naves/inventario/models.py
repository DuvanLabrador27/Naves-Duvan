from django.db import models

# Create your models here.
"""
    Clase nave que hereda de la clase models.Model,
    ademas es nuestra clase padre en nuestro modelo de naves
"""
class Nave(models.Model):
    #id = models.AutoField(primary_key=True)
    decisionesNaves = [('1','Vehiculo Lanzadera'),('2','Naves no tripuladas'),('3','Naves tripuladas')]
    nombreNave = models.CharField(max_length=50,verbose_name="Nombre de la nave")
    paisNave = models.CharField(max_length=50)
    pesoNave = models.CharField(max_length=50)
    alturaNave = models.CharField(max_length=50)
    velocidadNave = models.CharField(max_length=50)
    capacidadNave = models.CharField(max_length=50)
    potenciaNave = models.CharField(max_length=50)
    fecha = models.DateTimeField(blank=True, null=True)
    tipoNave = models.CharField(max_length=50,choices=decisionesNaves)

    def __str__(self):
        return self.nombreNave + " " + self.paisNave + " " + self.pesoNave + " " + self.alturaNave + " " + self.velocidadNave + " " + self.capacidadNave + " " + self.potenciaNave + " " + str(self.fecha) + " " + self.tipoNave
    
    class Meta:
        #Definimos que se abstracta para poder aplicar herencia
        abstract = True
        db_table = 'naves'
        verbose_name = "Nave"
        verbose_name_plural = "Naves"
        
"""
    Clase nave Lanzadera que hereda de la clase Nave
"""    
class naveLanzadera(Nave):
    #id = models.AutoField(primary_key=True)
    decisionesCarga = [('1','Satelite artificial'),('2','Sonda')]
    decisionesCombustible = [('1','Quimico Solido'),('2','Propelente Liquido')]
    tipoCarga = models.CharField(max_length=50,choices=decisionesCarga)
    tipoCombustible = models.CharField(max_length=50,choices=decisionesCombustible)
    

    class Meta:
        db_table = 'navesLanzadera'
        verbose_name = "Nave Lanzadera"
        verbose_name_plural = "Naves Lanzadera"

"""
    Clase nave no tripulada que hereda de la clase Nave
"""

class naveNoTripulada(Nave):
    #id = models.AutoField(primary_key=True)
    decisionesPlaneta = [('1','Saturno y sus lunas'),('2','Jupiter'),('3','Marte'),('4','Mercurio'),('5','pluton'),('6','Urano y Neptuno'),('7','Sol'),('8','Venus')]
    cantidadMotores = models.CharField(max_length=50)
    tipoPlaneta = models.CharField(max_length=50,choices=decisionesPlaneta)
    

    class Meta:
        db_table = 'navesNoTripulada'
        verbose_name = "Nave No Tripulada"
        verbose_name_plural = "Naves No Tripuladas"

"""
    Clase nave tripulada que hereda de la clase Nave
"""

class naveTripulada(Nave):
    #id = models.AutoField(primary_key=True)
    decisionesObjetivo = [('1','Misiones Lunares'),('2','Experimentación y estudio del comportamiento humano'),('3','Mantenimiento de satélites')]
    cantidadPersonas = models.CharField(max_length=50)
    tipoObjetivo = models.CharField(max_length=50,choices=decisionesObjetivo)
    

    class Meta:
        db_table = 'navesTripulada'
        verbose_name = "Nave Tripulada"
        verbose_name_plural = "Naves Tripuladas"
    
