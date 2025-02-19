from django.db import models

class Computador(models.Model):
    fabricante = models.CharField(max_length=100)
    processador = models.CharField(max_length=100)
    nucleos = models.IntegerField()
    memoria_ram = models.CharField(max_length=50)
    armazenamento = models.CharField(max_length=100)
    placa_video = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.fabricante} - {self.processador}"
