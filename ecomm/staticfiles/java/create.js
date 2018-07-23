

    $(document).on('submit','#form_id', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/logint',
        data:{
            name:$('#id_username').val(),
            password: $('#id_password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddilewaretoken]').val(),

        },
        success:function(){
        alert('login succesful');

        }
    });

    });