$(document).ready(function () {
    i=0
    $("#input").keypress(function () {
        $("#output").text(i += 1);
    });
    $("#input").hover(function () {
        b = $("#input").css("background-color");
        $("#input").css("background-color", "yellow");
        }, function () {
            $("#input").css("background-color", b);
        }
    );
});