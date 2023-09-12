var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var color = "black"
var score = 0;
var render = [];
var bullets = [];

const player = { x: 50, y: 50, width: 20, height: 20 ,color: color, speed: 5};
const bullet = { x: -10, y: 0, width: 5, height: 20 ,color: color, speed: 1};

// Function to check if two rectangles collide
function isRectCollision(rect1, rect2) {
  return (
    rect1.x < rect2.x + rect2.width &&
    rect1.x + rect1.width > rect2.x &&
    rect1.y < rect2.y + rect2.height &&
    rect1.y + rect1.height > rect2.y
  );
}

var keys = {
    ArrowRight: false,
    ArrowLeft: false,
    ArrowDown: false,
    ArrowUp: false,
    Space: false
};

function playerMovement() {
    if (keys.Space) {
        player.color = "red"
    } else {
        player.color = "black"
    }
    if (keys.ArrowRight) {
        player.x += player.speed;
    }
    if (keys.ArrowLeft) {
        player.x -= player.speed;
    }
    if (keys.ArrowDown) {
        player.y += player.speed;
    }
    if (keys.ArrowUp) {
        player.y -= player.speed;
    }
    if (player.x >= canvas.width + player.width + 5) {
        player.x = -player.width;
    }
    if (player.x <= -(player.width + 5)) {
        player.x = canvas.width + player.width;
    }
    if (player.y >= canvas.height + player.height + 5) {
        player.y = -player.height;
    }
    if (player.y <= -(player.height + 5)) {
        player.y = canvas.height + player.height;
    }
};

function shoot() {
    if (keys.Space && bullets.length < 5) {
        bullet.x = player.x + ( player.width /2-( bullet.width /2))
        bullet.y = player.y - player.height
        bullets.push(bullet);
    }

    for (let i = 0; i < bullets.length; i++) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < -bullets[i].height) {
            bullets.splice(i, 1);
            i--; // Adjust the index to account for the removed bullet
        }
    }
};

function main() {
    playerMovement();
    shoot()

    context.clearRect(0, 0, canvas.width, canvas.height);
    render = [player]

    for (var key in render) {
        if (render.hasOwnProperty(key)) {
            // Access the property key and its corresponding value
            var value = render[key];
            context.fillStyle = value.color
            context.fillRect(value.x, value.y, value.width, value.height);
        }
    }

    for (var i = 0; i < bullets.length; i++) {
        var bullet = bullets[i];
        context.fillStyle = bullet.color;
        context.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    }    

    context.fillStyle = "black"
    context.font = "50px Serif"
    context.fillText(score, 10, 50);

    requestAnimationFrame(main);
};

document.addEventListener("keydown", function(evt) {
    if (evt.code in keys) {
        keys[evt.code] = true;
    }
});

document.addEventListener("keyup", function(evt) {
    if (evt.code in keys) {
        keys[evt.code] = false;
    }
});

requestAnimationFrame(main);