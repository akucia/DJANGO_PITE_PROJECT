
// init default document structure
$( document ).ready(function() {
    loadDefaultBody();
    loadLoginPane();

    $(document).on('click', '.navMenuLink',function(event){
        var target=$(this).attr('href');

        $.get(target,function(data) {
            $("#pageHeader").html($(data).filter('#pageHeader'));
            $("#pageContent").html($(data).filter('#pageContent'));
        });

        event.preventDefault();
    });

    $(document).on('click', '.showLoginPane',function(){
        showLoginPane();
    });

    $(document).on('click','.hideLoginPane',function(){
        hideLoginPane();
    });

    $(document).on('click', '.insideNavLinkHide',function(event){
        event.preventDefault();
        $(this).removeClass("insideNavLinkHide");
        $(this).addClass("insideNavLinkShow");

        var target=$(this).attr('href');

        $("#"+target).hide();
    });

    $(document).on('click', '.insideNavLinkShow',function(event){
        event.preventDefault();
        $(this).addClass("insideNavLinkHide");
        $(this).removeClass("insideNavLinkShow");

        var target=$(this).attr('href');

        $("#"+target).show();
    });


    $(document).on('click','#logOutButton',function(){

        $.ajax({
            type: "GET",
            url: "hidden/jqLoginElements/logoutRequest",


            success : function(json){
                loadLoginPane();
                loadDefaultBody();
            }
        });

        event.preventDefault();
    });

});


function loadDefaultBody(){
    // load navigation menu
    $( "#navBar" ).load( "hidden/jqNavBar");

    // load default body
    $("#pageHeader").load( "hidden/jqDefault #pageHeader");
    $("#pageContent").load("hidden/jqDefault #pageContent");
    showLoginPane();
}
function loadLoginPane(){
    $("#pageContent").removeClass("col-sm-12");
    $("#pageContent").addClass("col-sm-8");
    $("#loginPane").show();

    $("#loginPane").load("hidden/jqLoginPane");

}

function showLoginPane(){
    $("#pageContent").removeClass("col-sm-12");
    $("#pageContent").addClass("col-sm-8");
    $("#loginPane").show();
}

function hideLoginPane(){
    $("#pageContent").addClass("col-sm-12");
    $("#loginPane").hide();
    $("#pageContent").removeClass("col-sm-8");
}