from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from models.models import User_Sala_Chat , Mensajes , Sala_Chat

class Home( View ):

	def get( self , request ):
		return render( request , 'home.html' )

	def post( self , request ):
		#Obtiene las salas de chat de este usuario donde es y no es administrador
		data_request = request.POST.dict()
		rows_user_chat_list = User_Sala_Chat.objects.filter( id_user=request.user )
		list_sala_chats = []
		for row_user_chat in rows_user_chat_list:
			Sala_Chat = row_user_chat.id_sala_chat #Tenemos el objeto Sala_Chat
			dict_sala_chat = {
			"id_sala_chat" : Sala_Chat.id ,
			"nombre" : Sala_Chat.nombre ,
			"fecha_creacion" : Sala_Chat.fecha_creacion ,
			"es_administrador" : row_user_chat.es_administrador }
			list_sala_chats.append( dict_sala_chat )
		return JsonResponse( {"sala_chat_user":list_sala_chats} )

class Chat( View ):

	def get( self , request , id_sala_chat ):
		list_queryset = User_Sala_Chat.objects.filter( id_user=request.user , id_sala_chat__id=id_sala_chat )
		if len(list_queryset)>0: #Existe un registro
			return render( request , 'chat.html' , {'id_sala_chat':id_sala_chat}) #Solo renderizamos la pagina chat
		return redirect('home')
	#La creacion de la sala de chat se hace desde el admin de Django


class MensajesView( View ):

	def get( self , request ):
		#obtiene los mensaje de un chat
		data_request = request.GET.dict()
		id_sala_chat = data_request["id_sala_chat"] #id_sala
		queryset_list = User_Sala_Chat.objects.filter( id_sala_chat__id=id_sala_chat , id_user=request.user )
		lista_mensajes_chat = []
		if len( queryset_list )>0: #Se encontraron registros
			list_queryset_mensajes = Mensajes.objects.filter( id_sala_chat__id=id_sala_chat ).order_by('fecha_mensaje')
			for row_mensaje in list_queryset_mensajes:
				dict_mensaje = {
					'id':row_mensaje.id,
					'user':{
						"id":row_mensaje.id_user_chat.id_user.id,
						"username":row_mensaje.id_user_chat.id_user.username,
					},
					
					'fecha_mensaje':row_mensaje.fecha_mensaje,
					'mensaje':row_mensaje.mensaje
				}
				lista_mensajes_chat.append( dict_mensaje )

		return JsonResponse( {"mensajes_chat":lista_mensajes_chat} )			


	def post( self , request ):
		#Ingresa un nuevo mensaje
		data_request = request.POST.dict()
		id_sala_chat = data_request["id_sala_chat"] #id_sala
		mensaje = data_request["mensaje"]
		#Existe ese registro en User_Sala_Chat que tiene ese usuario y ese chat, generamos el mensaje , en otro caso no
		queryset_list = User_Sala_Chat.objects.filter( id_sala_chat__id=id_sala_chat , id_user=request.user ) 
		if len( queryset_list )>0: #Se encontraron registros
			obj_new_mensaje = Mensajes(
				id_user_chat=queryset_list[0] ,
				mensaje=mensaje ,
				id_sala_chat=queryset_list[0].id_sala_chat )
			obj_new_mensaje.save()
			return JsonResponse( {"response":"Mensaje Guardado"} )

		return JsonResponse( {"response":"Error Mensaje No Guardado"} )
