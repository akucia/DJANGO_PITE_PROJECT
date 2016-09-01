$('#jq_login_form').on('submit', function(event){
            event.preventDefault();
            console.log("form submitted!")  // sanity check;


            $.ajax({
                    url : "hidden/jqLoginElements/loginRequest",
                    type : "POST",
                    data : {
                        email : $('#inputLoginEmail').val(),
                        password : $('#inputLoginPassword').val(),
                        csrfmiddlewaretoken: getCookie('csrftoken')
                    },

                    success : function(json) {
                        console.log(json);

                        var fieldMessages=Object.keys(json["fieldState"]);

                        if(json["successfullLogin"]==true){
                            loadLoginPane();
                            loadDefaultBody();
                        }

                        else{
                            markFieldAsCorrect("inputLoginEmail");
                            markFieldAsIncorrect("inputLoginPassword","");

                            fieldMessages.forEach(function(key){
                                console.log(key);
                                markFieldAsIncorrect(key,json["fieldState"][key]);
                            });

                        }
                    },

                    error : function(xhr,errmsg,err) {
                        alert("error");
                        console.log(xhr.status + ": " + xhr.responseText);
                    }
            });
        });
