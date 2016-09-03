$('#jq_surveyAnswer_check').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : "hidden/jqSurveyAnswer/checkIfUserIdIsCorrect",
        type : "POST",
        data : $("#jq_surveyAnswer_check").serialize(),

        success : function(json) {
            console.log(json);

            if(json['success']==true){
                var target = "hidden/jqSurveyAnswerForm?userID="+$("#surveyAnswerUserId").val();
                console.log(target);
                $.get(target,function(data) {
                    $("#pageHeader").html($(data).filter('#pageHeader'));
                    $("#pageContent").html($(data).filter('#pageContent'));
                });
            }

            else{
                markFieldAsIncorrect("surveyAnswerUserId",json['errorMSG'])
            }
        },

        error : function(xhr,errmsg,err) {
                        alert("error");
                        console.log(xhr.status + ": " + xhr.responseText);
                    }
    });
});




$('#jq_surveyAnswer_form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : "hidden/jqSurveyAnswer/checkIfUserIdIsCorrect",
        type : "POST",
        data : $("#jq_surveyAnswer_check").serialize(),

    });


});