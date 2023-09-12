var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var x = 150;
var y = 150;
var color = "black"
var score = 0;
var speed = 5;

var targets = {
    for (let i = 0; i > 5; i++) {
    
    }
    i1: {x: 0,y: 0,color, hit:0},
    i2: {x: 0,y: 0,color, hit:0},
    i3: {x: 0,y: 0,color, hit:0},
    i4: {x: 0,y: 0,color, hit:0},
    i5: {x: 0,y: 0,color, hit:0},
    i6: {x: 0,y: 0,color, hit:0}
}

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
    if (x >= canvas.width + 25) {
        x = -20;
    }
    if (x <= -25) {
        x = canvas.width + 20;
    }
    if (y >= canvas.height + 25) {
        y = -20;
    }
    if (y <= -25) {
        y = canvas.height + 20;
    }
};

function Targetcollision() {
    for (var key in targets) {
        if (targets.hasOwnProperty(key)) {
            // Access the property key and its corresponding value
            var value = targets[key];
            if (
                x >= value.x - 20 &&
                x <= value.x + 20 &&
                y >= value.y - 20 &&
                y <= value.y + 20
            ) {
                if (value.hit == 0){
                    value.hit = 1
                }
            }
        }
    }
};

function updateTarget() {
    for (var key in targets) {
        if (targets.hasOwnProperty(key)) {
            // Access the property key and its corresponding value
            var value = targets[key];
            if (value.hit != 0 &&
                value.hit < 40) {
                    value.color = `rgb(${value.hit * 10},0,0)`
                }
            if (value.hit == 40) {
                    value.hit = 0
                    value.color = "rgb(0,0,0)"
                    value.x = (Math.floor(Math.random() * 250))
                    value.y = (Math.floor(Math.random() * 250))
                    score++
                }
            }
            if (value.hit) {
                value.hit++
            }
            if (
                value.x == 0 &&
                value.y == 0
            ) {
                value.x = (Math.floor(Math.random() * 250))
                value.y = (Math.floor(Math.random() * 250))
            }
        }
    }

function main() {
    updateCubePosition();
    Targetcollision();
    updateTarget();

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillRect(x, y, 20, 20);

    for (var key in targets) {
        if (targets.hasOwnProperty(key)) {
            // Access the property key and its corresponding value
            var value = targets[key];
            context.fillStyle = value.color
            context.fillRect(value.x, value.y, 20, 20);
        }
    }

    context.fillStyle = "black"
    context.font = "50px Serif"
    context.fillText(score, 10, 50);

    requestAnimationFrame(main);
};

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