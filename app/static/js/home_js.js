$( document ).ready(function() {
    console.log( "Documento Cargado!" );
    obtener_chats_user( pinta_datos_sala_chat_user )
    
});

function obtener_chats_user( func_pinta_datos_sala_chats ){
    console.log( 'TOKEN CSRF_TOKEN' )
    console.log( CSRF_TOKEN )
    $.ajax({
        headers: {'X-CSRFToken': CSRF_TOKEN} ,
        url: url_sala_chats_user ,
        type:'post',
        data:{},
        dataType:'JSON',
        success: function( request ){
            console.log( "Exito Objetos Obtenidos!!!" )
            console.log( request )
            func_pinta_datos_sala_chats( request["sala_chat_user"] )
        },
        error: function( request ){
            console.log("Error Objetos no Obtenidos")
        },
    })

}


function pinta_datos_sala_chat_user( json_salas_chat ){
    
    lista_divs_sala_chats.forEach( divs_ingresados => {
        divs_ingresados.remove()
    });
    lista_divs_sala_chats = []
    
    json_salas_chat.forEach( data_chat => {
        let div_sala_chat_user = $("#Div_Sala_Chat_User").clone()
        $(div_sala_chat_user).attr("hidden",false)

        $(div_sala_chat_user).find("#fecha_creacion").text( String('Fecha Creacion: ' + data_chat["fecha_creacion"] ) )
        $(div_sala_chat_user).find("h2").text( data_chat["nombre"] )
        $(div_sala_chat_user).find("#id_sala_chat").text( data_chat["id_sala_chat"] )
        $(div_sala_chat_user).find("#es_administrador").text( data_chat["es_administrador"] )
        $(div_sala_chat_user).find("a").attr( "href" , url_sala_chat.replace("0",data_chat["id_sala_chat"]) )
        
        $( div_sala_chat_user ).insertBefore("#Div_Sala_Chat_User")

        lista_divs_sala_chats.push( div_sala_chat_user )

    }); 
}

function obtener_xml_user( func_pinta_datos_xmls_user ){
    $.ajax({
        url: url_obtener_xml_user ,
        type:'get',
        data:{},
        dataType:'JSON',
        success: function( request ){
            console.log( "Exito Objetos Obtenidos!!!" )
            console.log( request )
            func_pinta_datos_xmls_user( request["xml_user"] )
        },
        error: function( request ){
            console.log("Error Objetos no Obtenidos")
        },
    })

}

function descargar_xml_seleccionado(event){
    let div_xml_historial = event.target.parentNode.parentNode.parentNode
    id_xml = $(div_xml_historial).find("#id_xml").text() 
    console.log( url_descargar_xml_document.replace('0', id_xml )  )
    window.location.replace( url_descargar_xml_document.replace('0', id_xml ) );
}

function borrar_xml_seleccionado(event){
    let div_xml_historial = event.target.parentNode
    id_xml = $(div_xml_historial).find("#id_xml").text() 
    //console.log( url_borrar_xml_document.replace('0', id_xml )  )
    $.ajax({
        headers: {'X-CSRFToken': CSRF_TOKEN} ,
        url: url_borrar_xml_document ,
        type:'post',
        data:{ "id_xml":id_xml },
        dataType:'JSON',
        success: function( request ){
            console.log( "Exito Objetos Obtenidos!!!" )
            obtener_xml_user( pinta_datos_xmls_user )
        },
        error: function( request ){
            console.log("Error Objetos no Obtenidos")
        },
    })

}