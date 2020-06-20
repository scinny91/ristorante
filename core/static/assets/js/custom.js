jQuery( document ).ready(inizializza_tavoli)

function inizializza_tavoli()
{
    console.log('inizializzo tavoli')
    jQuery('#chiudi').click("chiudi_tavolo", manda_azione)
    jQuery('#consolida').click("consolida_tavolo", manda_azione)
    jQuery('#svuota').click("svuota_tavolo", manda_azione)
    jQuery('.pulsante_menu').click(aggiungi_piatto)
}


function manda_azione(request)
{
    console.log(request.data)
}

function aggiungi_piatto()
{
    formData= new FormData();
    formData.append('id_piatto', this.id)
    formData.append('id_tavolo', jQuery('#id_tavolo').val())


    jQuery.ajax(
        {
        url: "/aggiungi_piatto/",
        type: "POST",
        data: formData,
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        success: function(result)
            {
                console.log(result)
                if (result.status!=200)
                    alert(result.message)
            }
        ,
        fail: function(result)
            {console.log(result)}
        });
}