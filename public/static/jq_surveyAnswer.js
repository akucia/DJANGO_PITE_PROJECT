$('#jq_surveyAnswer_check').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : "hidden/jqSurveyAnswer/checkIfUserIdIsCorrect",
        type : "POST",
        data : {
            userID : $('#surveyAnswerUserId').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        },

        success : function(json) {
            console.log(json);

            if(json['success']==true){
                alert("UDAŁO Się redirect");
            }

            else{
                markFieldAsIncorrect("surveyAnswerUserId",json['errorMSG'])
            }

        }

        error : function(xhr,errmsg,err) {
                        alert("error");
                        console.log(xhr.status + ": " + xhr.responseText);
                    }


    });
});