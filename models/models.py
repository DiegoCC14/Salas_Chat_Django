from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Sala_Chat( models.Model ): #Contiene las salas de chats y sus administradores
	id = models.AutoField( primary_key=True )
	nombre = models.CharField( max_length=200 , blank=False )
	fecha_creacion = models.DateTimeField( default=datetime.now() )
	def __str__(self):
		return str(self.id) + " - " + self.nombre


class User_Sala_Chat( models.Model ): #Tabla que relaciona los usuarios con sus salas de chat
	id = models.AutoField( primary_key=True )
	id_sala_chat = models.ForeignKey( Sala_Chat , on_delete=models.CASCADE )
	id_user = models.ForeignKey( User , on_delete=models.CASCADE )
	fecha_ingreso = models.DateTimeField( default=datetime.now() )
	es_administrador = models.BooleanField()

class Mensajes( models.Model ):
	id = models.AutoField( primary_key=True )
	id_user_chat = models.ForeignKey( User_Sala_Chat , on_delete=models.CASCADE )
	id_sala_chat = models.ForeignKey( Sala_Chat , on_delete=models.CASCADE )
	fecha_mensaje = models.DateTimeField( default=datetime.now() )
	mensaje = models.CharField( max_length=2000 )