        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        $('#jq_register_form').on('submit', function(event){
            event.preventDefault();

            var nameValid=isNameValid();
            var surnameValid=isSurnameValid();
            var emailValid=isEmailValid();
            var passwordValid=isPasswordValid();

            if(nameValid && surnameValid && emailValid && passwordValid){

                console.log("form submitted!")  // sanity check;


                $.ajax({
                    url : "hidden/jqRegisterPanel/registerRequest",
                    type : "POST",
                    data : {
                        name : $('#inputName').val(),
                        surname : $('#inputSurname').val(),
                        email : $('#inputEmail').val(),
                        password : $('#inputPassword').val(),
                        rePassword: $('#inputPasswordRetype').val(),
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

                        markFieldAsCorrect("inputName");
                        markFieldAsCorrect("inputSurname");
                        markFieldAsCorrect("inputEmail");
                        markFieldAsCorrect("inputPassword");
                        markFieldAsCorrect("inputPasswordRetype");

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

            }
        });


        function isNameValid(){
            var toValidate=$("#inputName").val();
            var regExp=/^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{3,20}$/;
            var isValid=regExp.test(toValidate);

            if(isValid==false){
                markFieldAsIncorrect("inputName","Imię musi składać się z 3-20 liter");
            }
            else{
                markFieldAsUnknownState("inputName");
            }

            return isValid;
        }

        function isSurnameValid(){
            var toValidate=$("#inputSurname").val();
            var regExp=/^[A-Za-z àáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð,.'-]{3,50}$/;
            var isValid=regExp.test(toValidate);

            if(isValid==false){
                markFieldAsIncorrect("inputSurname","Nazwisko musi składać się z 3-50 liter i znaków");
            }
            else{
                markFieldAsUnknownState("inputSurname");
            }
            return isValid;
        }

        function isPasswordValid(){
            var toValidate=$("#inputPassword").val();
            var regExp=/(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;
            var isValid=regExp.test(toValidate);

            if(isValid==false){
                markFieldAsIncorrect("inputPassword","Hasło musi zawierać litery o różnej wielkości oraz cyfry i mieś długość co najmniej 6 znaków");
            }
            else if($("#inputPassword").val()!=$("#inputPasswordRetype").val()){
                isValid=false;
                markFieldAsIncorrect("inputPassword","Podane hasła nie są zgodne");
                markFieldAsIncorrect("inputPasswordRetype","");
            }
            else{
                markFieldAsUnknownState("inputPassword");
                markFieldAsUnknownState("inputPasswordRetype");
            }

            return isValid;
        }

        function isEmailValid(){
            var toValidate=$("#inputEmail").val();
            var regExp=/^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
            var isValid=regExp.test(toValidate);

            if(isValid==false){
                markFieldAsIncorrect("inputEmail","Wpisz e-mail w poprawnym formacie");
            }
            else{
                markFieldAsUnknownState("inputEmail");
            }
            return isValid;
        }