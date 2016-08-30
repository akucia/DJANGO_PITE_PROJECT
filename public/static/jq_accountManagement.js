$(".insideNavLinkHide").click(function(event) {
    event.preventDefault();
    $(this).removeClass("insideNavLinkHide");
    $(this).addClass("insideNavLinkShow");

    var target=$(this).attr('href');

    $("#"+target).hide();
});

$(".insideNavLinkShow").click(function(event) {
    event.preventDefault();
    $(this).addClass("insideNavLinkHide");
    $(this).removeClass("insideNavLinkShow");

    var target=$(this).attr('href');

    $("#"+target).show();
});