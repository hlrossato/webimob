$(function(){

	alugado();
});

function alugado(){

    var alugar = $('#alugar');
    var content = $('.mais');
    var slug = $(content).find("input[type='hidden']").val();    

    $(alugar).click(function(){

        $.ajax({
            type: 'POST',
            data: slug,
            url: "/imoveis/alugar/"+slug+"/"
        }).done(function(msg){
            if (msg == "reservado") {
                alert('Aeeeeeeeeeee');
            } else{
                alert('Fudeuuuu');
            }
        });
          

            // success: function (response) {
            //     alert('Aeeeeeeeeeeee');
            //     if (response == 'reservado') {
            //         showSuccessForm();

    	       //      setTimeout(function() {
    	       //          endSuccessForm();
    	       //      }, 3000);                
            //     } else{
            //     	showErrorForm();

    	       //      setTimeout(function() {
    	       //          showErrorForm();
    	       //      }, 3000);            	
            //     }
            // }
        // });
    });	
}

function showSuccessForm() {
    $('.msg-enviada').fadeIn();
}

function endSuccessForm() {
    $('.msg-enviada').fadeOut();   
}

function showErrorForm() {
    $('.msg-error').fadeOut();   
}