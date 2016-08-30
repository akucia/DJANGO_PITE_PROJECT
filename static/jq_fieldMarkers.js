
        function markFieldAsCorrect(ID){
            $("#"+ID).closest( ".form-group" ).removeClass("has-error");
            $("#"+ID).closest( ".form-group" ).removeClass("has-warning");
            $("#"+ID).closest( ".form-group" ).addClass("has-success");

            $("#"+ID).closest( ".form-group" ).addClass("has-feedback");

            $("#"+ID).parent().children(".glyphicon").removeClass("glyphicon-remove");
            $("#"+ID).parent().children(".glyphicon").removeClass( "glyphicon-warning-sign" );
            $("#"+ID).parent().children( ".glyphicon" ).addClass( "glyphicon-ok" );

            var message="";
            $("#"+ID).parent().parent().children( ".help-block" ).html(message);
        }

        function markFieldAsIncorrect(ID,message){
            $("#"+ID).closest( ".form-group" ).addClass("has-error");
            $("#"+ID).closest( ".form-group" ).removeClass("has-warning");
            $("#"+ID).closest( ".form-group" ).removeClass("has-success");

            $("#"+ID).closest( ".form-group" ).addClass("has-feedback");

            $("#"+ID).parent().children(".glyphicon").addClass("glyphicon-remove");
            $("#"+ID).parent().children(".glyphicon").removeClass( "glyphicon-warning-sign" );
            $("#"+ID).parent().children( ".glyphicon" ).removeClass( "glyphicon-ok" );

            $("#"+ID).parent().parent().children( ".help-block" ).html(message);
        }

        function markFieldAsUnknownState(ID){
            $("#"+ID).closest( ".form-group" ).removeClass("has-error");
            $("#"+ID).closest( ".form-group" ).removeClass("has-warning");
            $("#"+ID).closest( ".form-group" ).removeClass("has-success");

            $("#"+ID).closest( ".form-group" ).removeClass("has-feedback");

            $("#"+ID).parent().children(".glyphicon").removeClass("glyphicon-remove");
            $("#"+ID).parent().children(".glyphicon").removeClass( "glyphicon-warning-sign" );
            $("#"+ID).parent().children( ".glyphicon" ).removeClass( "glyphicon-ok" );

            var message="";
            $("#"+ID).parent().parent().children( ".help-block" ).html(message);
        }

        function markFieldAsCorrectWithText(ID,message){

            $("#"+ID).closest( ".form-group" ).removeClass("has-error");
            $("#"+ID).closest( ".form-group" ).removeClass("has-warning");
            $("#"+ID).closest( ".form-group" ).addClass("has-success");

            $("#"+ID).closest( ".form-group" ).addClass("has-feedback");

            $("#"+ID).parent().children(".glyphicon").removeClass("glyphicon-remove");
            $("#"+ID).parent().children(".glyphicon").removeClass( "glyphicon-warning-sign" );
            $("#"+ID).parent().children( ".glyphicon" ).addClass( "glyphicon-ok" );

            $("#"+ID).parent().parent().children( ".help-block" ).html(message);
        }

