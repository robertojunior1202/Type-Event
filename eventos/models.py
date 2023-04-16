from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True) #relação 1 -> muitos
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horaria = models.IntegerField()
    #logo = models.FileField() importa qualquer arquivo (usar para shape)
    logo = models.ImageField(upload_to='logos') #para importar imagens
    
    #paleta de cores
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)
    
    #Participantes
    participantes = models.ManyToManyField(User, related_name='evento_participante', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome
    
class Certificado(models.Model):
    certificado = models.ImageField(upload_to="certificados")
    participante = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)