$(function() {
    
    data_mask();

    $("#formulario").validate({
        onKeyUp: true,

        rules:{
            nome:{
                required: true, minlength: 3
            },
            email:{
                required: true, email: true
            },
            telefone:{
                required: true
            },
            data_nascimento:{
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
                url: "/clientes/pre-cadastro-clientes/send/",

                success: function (response) {
                    if (response == 'sucesso') {

                        showSuccessForm();
                        
                        hideLoading();
                        showButton();

                        emptyFields();                        
                        alteraCaptcha();
                    }
                    else{
                        window.location.href = '/clientes/cadastro-cliente/?c_id='+response;
                    }

                    setTimeout(function() {
                        endSuccessForm();
                    }, 3000);
                }
            });
        }            
    });
});

function data_mask(){

    var masks = ['(00) 00000-0000', '(00) 0000-00009'],
        maskBehavior = function(val, e, field, options) {
        return val.length > 14 ? masks[0] : masks[1];
    };

    $('#id_celular').mask(maskBehavior, {onKeyPress: 
       function(val, e, field, options) {
           field.mask(maskBehavior(val, e, field, options), options);
       }
    }); 
    
    $('#id_telefone').mask('(99) 9999-9999');
    $('#id_data_nascimento').mask('99/99/9999');
}

function emptyFields(){
    $("input[type='text'], textarea").val('');
}

function hideButton(){
    $('#enviar').hide();
    $('#continuar').hide();
}

function showButton(){
    $('#enviar').show();
    $('#continuar').show();
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