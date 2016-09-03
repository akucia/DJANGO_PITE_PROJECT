 $('#statsLink').bind('click', function(){
       setTimeout(function(){ drawAll(); }, 500);
  });

$('#jq_accoutDataChangeForm').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url: "hidden/jqAccountManagement/sentChangeUserdataRequest",
        type : "POST",
        data : {
            name : $('#changeNameInput').val(),
            surname : $('#changeSurnameInput').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success: function(json){
            console.log(json);

            if(json['success']==true){
                markFieldAsCorrect("changeSurnameInput");
                markFieldAsCorrectWithText("changeNameInput","Pomyślnie zmieniono dane osobowe");
                $("#accountSumUp").load("hidden/jqAccountManagement #accountSumUp >");

                setTimeout(function(){
                    markFieldAsUnknownState("changeSurnameInput");
                    markFieldAsUnknownState("changeNameInput");
                }, 3000);
            }
            else{
                markFieldAsCorrect("changeSurnameInput");
                markFieldAsCorrect("changeNameInput");

                var fieldMessages=Object.keys(json["fields"]);

                fieldMessages.forEach(function(key){
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

$('#jq_accoutPasswordChangeForm').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url: "hidden/jqAccountManagement/sentChangeUserPasswordRequest",
        type : "POST",
        data : {
            newPassword : $('#changeNewPasswordInput').val(),
            newPasswordRetype : $('#changeNewPasswordRetypeInput').val(),
            oldPassword : $('#changeOldPasswordInput').val(),

            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success: function(json){
            console.log(json);

            if(json['success']==true){
                markFieldAsCorrect("changeNewPasswordInput");
                markFieldAsCorrect("changeNewPasswordRetypeInput");
                markFieldAsCorrectWithText("changeOldPasswordInput","Pomyślnie zmieniono dane hasło");

                setTimeout(function(){
                    markFieldAsUnknownState("changeOldPasswordInput");
                    markFieldAsUnknownState("changeNewPasswordInput");
                    markFieldAsUnknownState("changeNewPasswordRetypeInput");
                }, 3000);
            }
            else{
                markFieldAsUnknownState("changeOldPasswordInput");
                markFieldAsUnknownState("changeNewPasswordInput");
                markFieldAsUnknownState("changeNewPasswordRetypeInput");

                var fieldMessages=Object.keys(json["fields"]);

                fieldMessages.forEach(function(key){
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

$('#accountSurveyList').on('click', '.removeSurvey',function(event){
    event.preventDefault();

    console.log( $(this).attr('href'));
    $.ajax({
        url: "hidden/jqAccountManagement/sentRemoveSurveyRequest",
        type : "POST",
        data : {
            adminID: $(this).attr('href'),
            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success: function(json){
                if(json["success"]==true){
                    $("#accountSurveyList").load("hidden/jqAccountManagement #accountSurveyList >");
                }
                console.log(json);

        },
        error : function(xhr,errmsg,err) {
                            alert("error");
                            console.log(xhr.status + ": " + xhr.responseText);
            }
    });
});