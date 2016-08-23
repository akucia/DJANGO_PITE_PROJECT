$('#jq_login_form').on('submit', function(event){
            event.preventDefault();
            console.log("form submitted!")  // sanity check;


            $.ajax({
                    url : "hidden/jqLoginElements/loginRequest",
                    type : "POST",
                    data : {
                        email : $('#inputEmail').val(),
                        password : $('#inputPassword').val(),
                        csrfmiddlewaretoken: getCookie('csrftoken')
                    },

                    success : function(json) {

                        console.log(json);
                        console.log(json["errorMSG"]);

                        var fieldMessages=Object.keys(json["fieldState"]);

                        if(json["successfullRegistration"]==true){
                            loadLoginPane();
                            loadDefaultBody();
                        }

                        markFieldAsCorrect("inputEmail");
                        markFieldAsCorrect("inputPassword");

                        fieldMessages.forEach(function(key){
                            console.log(key);
                            markFieldAsIncorrect(key,json["fieldState"][key]);
                        });
                    },

                    error : function(xhr,errmsg,err) {
                        alert("error");
                        console.log(xhr.status + ": " + xhr.responseText);
                    }
            });
        });