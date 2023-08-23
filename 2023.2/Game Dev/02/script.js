var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var image = new Image();
var image2 = new Image();

image.src = "img/ovni.png";
image2.src = "img/explosao.png";

var coords = [20,100,180,260,340]
var ships = [1, 1, 1, 1, 1];
var frameCounter = 0; // Counter to slow down animation

function main() {
    var x = 20;
    var y = 20;
    context.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
    for (var i = 0; i < 5; i++) {
        switch (ships[i]) {
            case 1:
                context.drawImage(image, x, y, 70, 40);
                break;
            case 2:
                context.drawImage(image2, 0, 15, 70, 50, x, y, 70, 40);
                ships[i] = 3;
                break;
            case 3:
                context.drawImage(image2, 70, 15, 70, 50, x, y, 70, 40);
                ships[i] = 4;
                break;
            case 4:
                context.drawImage(image2, 140, 15, 70, 50, x, y, 70, 40);
                ships[i] = 5;
                break;
            case 5:
                context.drawImage(image2, 210, 15, 70, 50, x, y, 70, 40);
                ships[i] = 0;
                break;
        }
        x += 80;
    }
    frameCounter++; // Increment the frame counter
    
    // Update the animation frames every 5 loops
    if (frameCounter % 5 === 0) {
        requestAnimationFrame(main);
        frameCounter = 0; // Reset the frame counter
    } else {
        setTimeout(function() {
            requestAnimationFrame(main);
        }, 150); // Wait for 100 milliseconds before requesting the next frame
    }
}

var mousePos = {
    x: null,
    y: null
}

document.addEventListener("mousemove", function(e) {
    mousePos.x = e.clientX;
  mousePos.y = e.clientY;
});

document.addEventListener("click", function(e) {
    for (var i = 0; i <= 5; i++) {
        if (
            mousePos.x > coords[i] &&
            mousePos.x < coords[i] + 80 &&
            mousePos.y > 30 &&
            mousePos.y < 70
        ) {
            if (ships[i] == 1) {
                ships[i] = 2;
            }
        }
    }
});

image.onload = function () {
    image2.onload = function () {
        main();
    };
};