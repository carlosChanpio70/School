var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

function main() {
  context.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
  context.beginPath();
  context.arc(50, 50, 25, .5 * Math.PI, 1.5 * Math.PI, false);
  context.arc(110, 50, 25, .5 * Math.PI, 1.5 * Math.PI, true);
  context.lineWidth = 2;
  context.strokeStyle = "dark";
  context.fillStyle = "grey";
  context.fill();
  context.stroke();
}

main();
