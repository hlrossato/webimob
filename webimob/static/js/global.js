function alteraCaptcha(complete){
    $.post("/alteraImgCaptcha/",{

        },function( response ){
            var response = $( '<div>'+response+'</div>' ).find('img').attr('src');  
            $('img.captcha').attr('src', response)

            if (complete){
                complete();
            }
    });
}


jQuery(function(){
    jQuery('.camera_wrap').camera({
        height: '450px',
        pagination: false,
        playPause: false,
        overlayer: false,
        hover: false,
        thumbnails: false,
        navigation: false,
        loader: 'none'
    });    
});