from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Sala_Chat , User_Sala_Chat , Mensajes



@admin.register( Sala_Chat )
class Sala_Chat_Admin(admin.ModelAdmin):
	list_display = ( 'id' , 'nombre' ,'fecha_creacion' )
	fields = ( 'nombre', ) #Ahora el id_user se ingresa en save_model	

	def save_model(self, request, obj , form , change ): #Sobreescritura de metodo guardado
		super( Sala_Chat_Admin , self).save_model( request, obj, form, change ) #guardams el registro, normalmente
		objRowUserSalaChat = User_Sala_Chat(
			id_sala_chat = obj ,
			id_user = request.user ,
			es_administrador = True
		)
		objRowUserSalaChat.save() #Guardamos el usuario en UserSalaChat como administrador de esta sala

	def get_queryset(self, request ): #Sobreescritura de metodo mostrar lista de objetos
		if request.user.is_superuser:
			return Sala_Chat.objects.all() #Si sos superUsuario podes ver todas las Salas Cradas
		
		UserSalaChat_InerJoin_SalaChat = User_Sala_Chat.objects.select_related( 'id_sala_chat' ).filter( id_user=request.user , es_administrador=True ) #INNER JOIN con table Sala Chat , #tablas donde user es admin 
		return Sala_Chat.objects.filter( id__in=[row.id_sala_chat.id for row in UserSalaChat_InerJoin_SalaChat] ) #Solo veras las salas donde eres admin


@admin.register( User_Sala_Chat )
class User_Sala_Chat_Admin(admin.ModelAdmin):
	list_display = ( 'id' , 'id_sala_chat' , 'id_user' , 'fecha_ingreso' , 'es_administrador' )
	fields = ( 'id_sala_chat' , 'id_user' , 'es_administrador' ) #Ahora el id_user se ingresa en save_model

	def get_form(self, request, obj=None, **kwargs):
		form = super( User_Sala_Chat_Admin, self).get_form( request, obj=obj , **kwargs )
		
		List_Salas_Chats = User_Sala_Chat.objects.select_related( 'id_sala_chat' ).filter( id_user=request.user , es_administrador=True )
		form.base_fields['id_sala_chat'].queryset = Sala_Chat.objects.filter( id__in=[row.id_sala_chat.id for row in List_Salas_Chats] )
		return form
	
	def get_queryset(self, request ): #Sobreescritura de metodo mostrar lista de objetos
		if request.user.is_superuser:
			return User_Sala_Chat.objects.all() #Si sos superUsuario podes ver todas las Salas Cradas
		
		UserSalaChat_currentuser = User_Sala_Chat.objects.filter( id_user=request.user ) #INNER JOIN con table Sala Chat , #registros sala donde esta incorporado este usuario
		return User_Sala_Chat.objects.filter( id_sala_chat__in=[row.id_sala_chat for row in UserSalaChat_currentuser] ) #Solo veras las salas donde eres admin
	

@admin.register( Mensajes )
class Mensajes_Admin(admin.ModelAdmin):
	list_display = ( 'id' , 'id_user_chat' , 'fecha_mensaje' , 'mensaje' )
