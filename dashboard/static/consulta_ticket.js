function consulta_agente(id_agente){
    $.ajax({


        type: 'GET',
        url: 'https://fotosensores-dnit.freshdesk.com/api/v2/agents/'+id_agente+'',
        dataType: 'json',
        headers :{
            'Authorization': 'Basic ' + btoa('COuIBILolWo6vqXmL9R0' + ':x')
        },

        success: function(data, textStatus, jqXHR) {
          $('#result').text('Success');
          $('#code').text(jqXHR.status);

          if(data.id == id_agente){

            if(data.contact.hasOwnProperty("avatar")){
               $('.user_id.'+id_agente).each(function( index ){   
                    
                   
                   $(this).html('<img src="'+data.contact.avatar.thumb_url+'" style="left: 10px; height:auto; border-radius:50px; position:relative; width:50px;">')
                   $(this).append('<text style="margin: auto;">'+data.contact.name+'</text>')

                   var user_email = $("#user_email").val()
                    if(data.contact.email == user_email){
                        $(this).css("margin-left","auto");
                        $(this).css({'background':'#D1F8D1', 'box-shadow': '0 0 1em green'})
                        $('.resposta.'+id_agente).css({'background':'#D1F8D1'})
                        $('.resposta.'+id_agente+ ' div').css({'background':'#D1F8D1'})

                    } 
               });

            }else{
               $('.user_id.'+id_agente).each(function( index ){
                   $(this).html('<div style="left: 10px; background: red; height:50px; border-radius:50px; position:relative; width:50px; margin:auto; text-align: center; color: white; font-size: xx-large; font-weight: bold;">'+data.contact.name[0]+'</div>')
                   $(this).append('<text style="margin: auto;">'+data.contact.name+'</text>')
                   var user_email = $("#user_email").val()
                    if(data.contact.email == user_email){
                        $(this).css("margin-left","auto");
                        $(this).css({'background':'#D1F8D1', 'box-shadow': '0 0 1em green'})
                        $('.resposta.'+id_agente).css({'background':'#D1F8D1'})
                        $('.resposta.'+id_agente+ ' div').css({'background':'#D1F8D1'})



                    }
               });


            }

            


          // $('.user_id#'+id_agente).append('<text style="margin: auto;">'+data.contact.name+'</text>')


          }


        },

        complete: function (jqXHR){

            if (jqXHR.status == '401') {

                console.log('a')
            }


        },
    });


}


function consulta_ticket(id_ticket){
    $.ajax({


        type: 'GET',
        url: 'https://fotosensores-dnit.freshdesk.com/api/v2/tickets/' + id_ticket + '?include=conversations',
        dataType: 'json',
        headers :{
            'Authorization': 'Basic ' + btoa('COuIBILolWo6vqXmL9R0' + ':x')
        },

        success: function(data, textStatus, jqXHR) {
          $('#result').text('Success');
          $('#code').text(jqXHR.status);


          $('#descricao').html(data.description)
          
            if(data.conversations.length > 0){
                $(data.conversations).each(function( index ){
                    let d = new Date(data.conversations[index].updated_at);
                    var horas = d.getHours();
                    var minutos = d.getMinutes();

                    if(horas < 10){

                        horas = "0" + horas;

                    }

                    if(minutos < 10){

                        minutos = "0" + minutos;

                    }

                    let data_atualizacao = ((d.getDate() )) + "/" + ((d.getMonth() + 1)) + "/" + d.getFullYear() + " " + horas + ":" + minutos;

                    consulta_agente(data.conversations[index].user_id)


                    $('.modal.show #respostas').append('<div class="user_id ' + data.conversations[index].user_id + '" style="box-shadow: 0 0 1em; height: 60px; display: grid; grid-template-columns: 0.2fr 1fr;" ></div><div class="resposta ' + data.conversations[index].user_id + '" style="position: relative; min-height: 200px; padding:5px; box-shadow: 0 0 1em;"> ' + data.conversations[index].body + '<text style="right: 20px; position: absolute; bottom: 0;" >Data: '+ data_atualizacao +'</text></div><div class="spacer"></div>')
                    //$('#respostas .user_id').append(data.conversations[index].body)


                    $('#respostas .user_id div').css("width","100%");
                    $('#respostas div').css("text-align","justify");
                    $('#respostas div').css("background","#efefef");
                    $('#respostas div').css("margin","20px");
                    $('#respostas div').css("border-radius","20px");
                    $('#respostas div').css("font-size","17px");
                    $('#respostas img ').css("width","100%");

                    $('#descricao').css("background","#FFF");
                    $('#descricao').css("border-radius","20px");
                    $('#descricao').css("min-height","200px");
                    $('#descricao').css("padding","20px");
                    $('#descricao').css("font-size","15px");

                    $('#respostas .user_id').css("padding","5px");
                    $('#respostas .user_id').css("width","30%");
                    $('#respostas .user_id img').css("margin","0 20px");

                    $('#descricao div div img').css("width","100%");
                    $('#descricao div').css("font-size","17px");
                    $('#descricao div').css("font-weight","bold");


                });

            }else{

                $('#respostas').html('<p>Sem respostas para este ticket</p>')

            }

        },

        complete: function (jqXHR){

            if (jqXHR.status == '401') {

                console.log('A')

            }


        },

    });
}

function reseta_respostas_modal(){

    $('#respostas').html('');
    $('#link_freshdesk').html('');

}

function renova_loading(){

    var fadeContainer = document.querySelector("#fade-container");
    fadeContainer.removeAttribute("style")

}

function loading(){
var fadeContainer = document.querySelector("#fade-container");

  setTimeout(function() {

        fadeContainer.style.display = "none";

  }, 1500);

}


$(".box_ticket").hover(function(){
    var myClasses = this.classList;
    if($('.lastReply_'+myClasses[1]).text() == ''){
        addLastReply(myClasses[1])
    }
    
    $('.hideTicket.'+myClasses[1]).show();
    
},function(){
    $('.hideTicket').hide();
});

function addLastReply(id_ticket){
    $.ajax({


        type: 'GET',
        url: 'https://fotosensores-dnit.freshdesk.com/api/v2/tickets/' + id_ticket + '?include=conversations',
        dataType: 'json',
        headers :{
            'Authorization': 'Basic ' + btoa('COuIBILolWo6vqXmL9R0' + ':x')
        },

        success: function(data, textStatus, jqXHR) {
          $('#result').text('Success');
          $('#code').text(jqXHR.status);
          
          
          if(data.conversations.length > 0){

          addLastReplyUser(data.conversations[data.conversations.length - 1].user_id, id_ticket)
          $('.lastReply_'+id_ticket).html(data.conversations[data.conversations.length - 1].body_text)
        }else{
          
          if(data.requester_id == 67033817683){

            $('.lastReplyUser_'+id_ticket).css('display','flex')

            $('.lastReplyUser_'+id_ticket).html('<div style="left: 10px; background: green; height:50px; border-radius:50px; position:relative; width:50px; text-align: center; color: white; font-size: xx-large; font-weight: bold;left: 10px; height:auto; border-radius:50px; position:relative; width:50px !important;">E</div>')
                                                
            $('.lastReplyUser_'+id_ticket).append('<text style="margin: 12px 30px; left:0;">Supervisão Operações "ETEL"</text>')

          }else{


            addLastReplyUser(data.requester_id, id_ticket) 

          }
          
          $('.lastReply_'+id_ticket).html(data.description_text)

        }



        },






        });
    }


function addLastReplyUser(id_agente, id_ticket){
        $.ajax({
    
    
            type: 'GET',
            url: 'https://fotosensores-dnit.freshdesk.com/api/v2/agents/'+id_agente+'',
            dataType: 'json',
            headers :{
                'Authorization': 'Basic ' + btoa('COuIBILolWo6vqXmL9R0' + ':x')
            },
    
            success: function(data, textStatus, jqXHR) {
              $('#result').text('Success');
              $('#code').text(jqXHR.status);

    
              if(data.id == id_agente){
    
                if(data.contact.hasOwnProperty("avatar")){                     
                       
                    $('.lastReplyUser_'+id_ticket).html('<img src="'+data.contact.avatar.thumb_url+'" style="left: 10px; height:auto; border-radius:50px; position:relative; width:50px !important;">')
                    $('.lastReplyUser_'+id_ticket).append('<text style="margin-left: 20px;">'+data.contact.name+'</text>')

                }else{
                       $('.lastReplyUser_'+id_ticket).css('display','flex')
                       $('.lastReplyUser_'+id_ticket).html('<div style="left: 10px; background: green; height:50px; border-radius:50px; position:relative; width:50px; text-align: center; color: white; font-size: xx-large; font-weight: bold;left: 10px; height:auto; border-radius:50px; position:relative; width:50px !important;">'+data.contact.name[0]+'</div>')
                       $('.lastReplyUser_'+id_ticket).append('<text style="margin: 12px 30px;">'+data.contact.name+'</text>')
    
    
                }
    
                
    
    
              // $('.user_id#'+id_agente).append('<text style="margin: auto;">'+data.contact.name+'</text>')
    
    
              }
    
    
            },
    
            complete: function (jqXHR){
    
                if (jqXHR.status == '401') {
    
                    console.log('a')
                }
    
    
            },
        });
    
    
    }


