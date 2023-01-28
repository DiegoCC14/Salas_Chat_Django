$( document ).ready(function() {
    console.log( "Documento Cargado!" );
    //enviar_mensaje()
    obtener_mensajes_sala_chat( pinta_los_mensajes_de_sala_chat )
    
});


function enviar_mensaje( event ){
	let mensaje= $("#mensaje_a_enviar").val();
	if ( event.key==="Enter" ){
		$.ajax({
			headers: {'X-CSRFToken': CSRF_TOKEN} ,
	        url: url_mensajes_sala_chat ,
	        type:'post',
	        data:{
	        	'mensaje' : mensaje,
	        	'id_sala_chat' : id_sala_chat
	        },
	        dataType:'JSON',
	        success: function( request ){
	            console.log( "Exito Mensaje Enviado!!!" )
	            console.log( request )
	            obtener_mensajes_sala_chat( pinta_los_mensajes_de_sala_chat )
	            //func_pinta_datos_sala_chats( request["sala_chat_user"] )
	        },
	        error: function( request ){
	            console.log("Error Objetos no Obtenidos")
	        },
		})

		$("#mensaje_a_enviar").val("");
	}
}


//function obtener_chats_user( func_pinta_datos_sala_chats ){
function obtener_mensajes_sala_chat( func_pinta_datos_sala_chats ){
    $.ajax({
        url: url_mensajes_sala_chat ,
        type:'get',
        data:{
        	'id_sala_chat':id_sala_chat
        },
        dataType:'JSON',
        success: function( request ){
            console.log( "Exito Mensajes Obtenidos!!!" )
            console.log( request )
            func_pinta_datos_sala_chats( request["mensajes_chat"] )
        },
        error: function( request ){
            console.log("Error Objetos no Obtenidos")
        },
    })

}

function pinta_los_mensajes_de_sala_chat( list_mensajes ){
	lista_divs_historial.forEach( divs_ingresados => {
        divs_ingresados.remove()
    });
    
    lista_divs_historial = []

	list_mensajes.forEach( mensaje => {
		
		if ( String(mensaje['user']['id']) === String(id_user) ){
			
			let div_mensaje_usuario_actual = $("#mensaje_usuario_actual").clone()

	        $(div_mensaje_usuario_actual).attr("hidden",false)

	        $(div_mensaje_usuario_actual).find("p").text( mensaje['mensaje'] )

	        $(div_mensaje_usuario_actual).find("span").text( mensaje['fecha_mensaje'])

	        $( div_mensaje_usuario_actual ).insertBefore("#ultimo_div_ingresado")
	        
	        lista_divs_historial.push( div_mensaje_usuario_actual )

		}else{
	        let div_mensaje_otro_usuario = $("#mensaje_otros_usuarios").clone()
	        $(div_mensaje_otro_usuario).attr("hidden",false)

	        $(div_mensaje_otro_usuario).find("p").text( mensaje['mensaje'] )

	        $(div_mensaje_otro_usuario).find("#username").text( mensaje['user']["username"] )
	        
	        $(div_mensaje_otro_usuario).find("span").text( mensaje['fecha_mensaje'] )

	        $( div_mensaje_otro_usuario ).insertBefore("#ultimo_div_ingresado")
	        
	        lista_divs_historial.push( div_mensaje_otro_usuario )
		}

    });

}