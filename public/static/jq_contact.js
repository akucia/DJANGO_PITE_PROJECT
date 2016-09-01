
        $('#jq_contactForm').on('submit', function(event){
            event.preventDefault();


                console.log("form submitted!")  // sanity check;

                var allValid=true;

                var name=$('#contactName').val();
                var surname=$('#contactSurname').val();
                var email=$('#contactEmail').val();


                if(isName(name)){
                    markFieldAsUnknownState("contactName");
                }
                else{
                    allValid=false;
                    markFieldAsIncorrect("contactName","Imię musi składać się z 3-20 liter");
                }

                if(isSurname(surname)){
                    markFieldAsUnknownState("contactSurname");
                }
                else{
                    allValid=false;
                    markFieldAsIncorrect("contactSurname","Nazwisko musi składać się z 3-50 liter i znaków");
                }

                if(isEmail(email)){
                    markFieldAsUnknownState("contactEmail");
                }
                else{
                    allValid=false;
                    markFieldAsIncorrect("contactEmail","Wpisz e-mail w poprawnym formacie");
                }

                if(!allValid){
                    return;
                }

                $.ajax({
                    url : "hidden/jqContactForm/contactSentMailRequest",
                    type : "POST",
                    data : {
                        name : name,
                        surname : surname,
                        email : email,
                        text : $('#contactText').val(),
                        topic : $('#contactTopic').val(),
                        captcha_0 : $('#id_captcha_0').val(),
                        captcha_1 : $('#id_captcha_1').val(),
                        csrfmiddlewaretoken: getCookie('csrftoken')
                    },

                    success : function(json) {

                        console.log(json);
                        console.log(json["errorMSG"]);

                        var fieldMessages=Object.keys(json["fieldState"]);

                        if(json["successful"]==true){
                            $("#messagePane").removeClass("alert-danger");
                            $("#messagePane").addClass("alert-success");
                            $("#messagePane").html("<strong>Success! </strong> Dziękujemy za skontatkowanie się z nami. Odpowiedź otrzymasz najszybciej jak się da.");
                            $("#messagePane").fadeIn(1000);

                            setTimeout(function(){ $("#messagePane").fadeOut(1000); }, 5000);

                        }
                        else{
                            $("#messagePane").addClass("alert-danger");
                            $("#messagePane").removeClass("alert-success");
                            $("#messagePane").html("<strong>Błąd!  </strong> "+json["errorMSG"]);
                            $("#messagePane").fadeIn(1000);

                            setTimeout(function(){ $("#messagePane").fadeOut(1000); }, 5000);

                        }

                        $("#captchaFieldElement").load("hidden/jqContactForm #captchaFieldElement > ");


                        markFieldAsCorrect("contactName");
                        markFieldAsCorrect("contactSurname");
                        markFieldAsCorrect("contactEmail");
                        markFieldAsCorrect("contactText");
                        markFieldAsCorrect("contactTopic");

                        fieldMessages.forEach(function(key){
                            console.log(key);
                            markFieldAsIncorrect(key,json["fieldState"][key]);
                        });
                    },

                    error : function(xhr,errmsg,err) {
                        console.log(xhr.status + ": " + xhr.responseText);
                    }
                });


        });

