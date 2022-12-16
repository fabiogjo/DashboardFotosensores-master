from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Usuario(AbstractUser):
    class Meta:
        db_table = 'Usuarios'
    
    nome = models.CharField(max_length=20, blank=False, null=False)
    sobrenome = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    chave_freshdesk = models.CharField(max_length=50, blank=False, null=False)
    celular = models.CharField(max_length=50, blank=False, null=False)
    foto = models.ImageField(upload_to='fotos/', blank=True)
    
    
    def get_full_name(self):
        return f'{self.nome} {self.sobrenome}'
    

