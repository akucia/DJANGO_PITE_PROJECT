$('#jq_restorePassword_email').on('submit', function(event){
    event.preventDefault();


    if(!isEmail($('#restoreEmail').val())){
        markFieldAsIncorrect("restoreEmail","Wpisz e-mail w poprawnym formacie");
        $("#secretCode").prop('disabled', true);
        $("#restorePassword").prop('disabled', true);
        $("#restorePasswordRetype").prop('disabled', true);
        $("#step2Submit").prop('disabled', true);

        return;
    }

    $.ajax({
        url : "hidden/jqRestorePassword/sentRestoreEmailRequest",
        type : "POST",


        data : {
            email : $('#restoreEmail').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success : function(json) {
            console.log(json);

            if(json['success']==false){
                markFieldAsIncorrect("restoreEmail",json['emailMessage']);
                $("#secretCode").prop('disabled', true);
                $("#restorePassword").prop('disabled', true);
                $("#restorePasswordRetype").prop('disabled', true);
                $("#step2Submit").prop('disabled', true);
            }
            else{
                markFieldAsCorrectWithText("restoreEmail",json['emailMessage']);
                $("#secretCode").prop('disabled', false);
                $("#restorePassword").prop('disabled', false);
                $("#restorePasswordRetype").prop('disabled', false);
                $("#step2Submit").prop('disabled', false);
                $("#step1Submit").prop('disabled', true);
                $("#restoreEmail").prop('disabled', true);
            }
        },

        error : function(xhr,errmsg,err) {
            alert("error");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
});



$('#jq_restorePassword_newPassword').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : "hidden/jqRestorePassword/sentNewPasswordRequest",
        type : "POST",

        data : {
            secretCode : $('#secretCode').val(),
            restorePassword : $('#restorePassword').val(),
            restorePasswordRetype : $('#restorePasswordRetype').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success : function(json) {
            console.log(json);

            if(json['success']==true){
                markFieldAsCorrectWithText("secretCode","Odzyskiwanie przebiegło pomyślnie");
                markFieldAsCorrect("restorePassword");
                markFieldAsCorrect("restorePasswordRetype");

                $("#secretCode").prop('disabled', true);
                $("#restorePassword").prop('disabled', true);
                $("#restorePasswordRetype").prop('disabled', true);
                $("#step2Submit").prop('disabled', true);
            }
            else{
                markFieldAsCorrect("secretCode");
                markFieldAsCorrect("restorePassword");
                markFieldAsCorrect("restorePasswordRetype");

                var fieldMessages=Object.keys(json["fields"]);

                fieldMessages.forEach(function(key){
                            console.log(key);
                            markFieldAsIncorrect(key,json["fields"][key]);
                    });
            }

        },

        error : function(xhr,errmsg,err) {
            alert("error");
            console.log(xhr.status + ": " + xhr.responseText);
        }

    });
});





