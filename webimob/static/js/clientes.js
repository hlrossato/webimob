$(function(){
    data_mask();

    $("#formulario").validate({
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
            },
            rg:{
                required: true
            },
            cpf:{
                required: true
            },
            endereco:{
                required: true
            },
            cidade:{
                required: true
            },
            estado:{
                required: true
            },
            estado_civil:{
                required: true
            },
            profissao:{
                required: true
            },
            faixa_salarial:{
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
                url: "/clientes/cadastro-cliente/send/",

                success: function (response) {
                    if (response == 'sucesso') {

                        showSuccessForm();
                        
                        showButton();
                        hideLoading();

                        emptyFields();
                    }
                    else{
                        alert('Este CPF já existe!');
                        hideLoading();
                        showButton();
                        $('html, body').animate({
                            scrollTop: $('#id_cpf').offset().top
                        }, 500);
                        $('#id_cpf').addClass('error');                        
                        $('#id_cpf').val('');                        
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

    $('#id_celular_conjuge').mask(maskBehavior, {onKeyPress: 
       function(val, e, field, options) {
           field.mask(maskBehavior(val, e, field, options), options);
       }
    }); 
    
    $('#id_telefone').mask('(99) 9999-9999');
    $('#id_telefone_conjuge').mask('(99) 9999-9999');
    $('#id_data_nascimento').mask('99/99/9999');
    $('#id_data_nascimento_conjuge').mask('99/99/9999');
    $('#id_cpf').mask('999.999.999-99');
    $('#id_rg').mask('99.999.999-99');
    $('#id_faixa_salarial').maskMoney({prefix:"R$ ", decimal:",", thousands:"."});
}

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
    $('#formulario').fadeOut();
    $('.msg-enviada').fadeIn();
}

function endSuccessForm() {
    $('.msg-enviada').fadeOut();
    $('#formulario').fadeIn();
}