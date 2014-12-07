$(function() {
    
    $("#formulario").validate({
        onKeyUp: true,
        rules:{
            login:{
                required: true, minlength: 3
            },
            senha:{
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
                url: "/logado/",

                success: function (response) {
                    if (response == 'sucesso') {

                        showSuccessForm();
                        
                        showButton();
                        hideLoading();
                    }
                    else{
                        hideLoading();
                        showButton();
                        emptyFields();
                        addErrors();
                    }
                }
            });
        },      
    });    
});

function addErrors(){
    $('#id_login').addClass('error');
    $('#id_senha').addClass('error');
}

function emptyFields(){
    $("input[type='password'], textarea").val('');
}

function hideButton(){
    $('#login').hide();
}

function showButton(){
    $('#login').show();
}

function hideLoading(){
    $('.loading').hide();
}

function showLoading(){
    $('.loading').show();
}

function showSuccessForm() {
    window.location = ('/area-restrita/');
}