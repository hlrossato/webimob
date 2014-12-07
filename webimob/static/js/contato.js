$(function() {
    
    $("#formulario").validate({
        onKeyUp: true,
        rules:{
            assunto:{
                required: true
            },
            nome:{
                required: true, minlength: 3
            },
            email:{
                required: true, email: true
            },                
            mensagem:{
                required: true, minlength: 3
            },
            captcha_1:{
                required: true
            }
        },

        submitHandler: function(form) {
            var form = $('#formulario');

            showLoading();
            hideButton();
            
            $.ajax({
                type: 'POST',
                data: form.serialize(),
                url: "/contato/send/",

                success: function (response) {
                    if (response == 'sucesso') {

                        showSuccessForm();
                        
                        showButton();
                        hideLoading();

                        emptyFields();                        
                        alteraCaptcha();
                    }

                    setTimeout(function() {
                        endSuccessForm();
                    }, 3000);
                }
            });
        }            
    });
});

function emptyFields(){
    $("input[type='text'], textarea").val('');
}

function hideButton(){
    $('#enviar').hide();
}

function showButton(){
    $('#enviar').show();
}

function hideLoading(){
    $('.loading').hide();
}

function showLoading(){
    $('.loading').show();
}

function showSuccessForm() {
    $('.msg-enviada').fadeIn();
}

function endSuccessForm() {
    $('.msg-enviada').fadeOut();   
}