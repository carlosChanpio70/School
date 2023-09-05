var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var x = 100;
var y = 100;
var speed = 5;

var keys = {
    ArrowRight: false,
    ArrowLeft: false,
    ArrowDown: false,
    ArrowUp: false
};

function updateCubePosition() {
    if (keys.ArrowRight) {
        x += speed;
    }
    if (keys.ArrowLeft) {
        x -= speed;
    }
    if (keys.ArrowDown) {
        y += speed;
    }
    if (keys.ArrowUp) {
        y -= speed;
    }
    if (x >= 325) {
        x = -20;
    }
    if (x <= -25) {
        x = 320;
    }
    if (y >= 355) {
        y = -50;
    }
    if (y <= -55) {
        y = 350;
    }
}

function main() {
    updateCubePosition();

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillRect(x, y, 20, 50);

    requestAnimationFrame(main);
}

document.addEventListener("keydown", function(evt) {
    if (evt.key in keys) {
        keys[evt.key] = true;
    }
});

document.addEventListener("keyup", function(evt) {
    if (evt.key in keys) {
        keys[evt.key] = false;
    }
});

requestAnimationFrame(main);