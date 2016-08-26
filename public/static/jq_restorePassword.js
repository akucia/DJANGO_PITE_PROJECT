$('#jq_restorePassword_email').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : "hidden/jqRestorePassword/sentRestoreEmailRequest",
        type : "POST",


        data : {
            email : $('#inputName').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success : function(json) {
            console.log(json);




        },

        error : function(xhr,errmsg,err) {
            alert("error");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });


