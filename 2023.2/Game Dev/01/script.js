function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

canvas.addEventListener("mousemove", function(evt) {
    var pos = getMousePos(canvas, evt);
    
    context.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
    context.beginPath();
    context.arc(pos.x, pos.y, 25, 0, 2 * Math.PI, false);
    context.lineWidth = 2;
    context.strokeStyle = "red";
    context.stroke();
});