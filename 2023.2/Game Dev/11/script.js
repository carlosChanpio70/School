var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var color = "white";
var bullets = [];
var targets = [];
var background = new Image();
background.src = "background.png";

//? Return random number between 2 numbers
function getRandom(n0, n1) {
  var n2 = n1;
  if (n0 > n1) {
    n1 = n0;
    n0 = n2;
  }
  return Math.random() * (n1 - n0) + n0;
}

//? Check collision between 2 objects
function isRectCollision(rect1, rect2) {
  return (
    rect1.x < rect2.x + rect2.width &&
    rect1.x + rect1.width > rect2.x &&
    rect1.y < rect2.y + rect2.height &&
    rect1.y + rect1.height > rect2.y
  );
}

var start_y = canvas.height / 2;
var max_health = 3;
const player = {
  x: canvas.width / 2,
  y: start_y,
  width: 40,
  height: 20,
  color: "red",
  speed: 2,
  moveleft: 1,
  moveright: 1,
  moveup: 1,
  movedown: 1,
  direction: 2,
  cooldown: 0.5,
  image: new Image(),
  health: max_health,
};
const target_model = {
  x: canvas.width / 2,
  y: 0,
  width: 40,
  height: 20,
  color: color,
  speed: 2,
  direction: 1,
  image: new Image(),
};
const bullet_model = {
  x: -10,
  y: 0,
  width: 5,
  height: 20,
  color: color,
  speed: 10,
};

player.image.src = "player.png";
target_model.image.src = "enemy.png";

for (var i = 0; i < 25; i++) {
  targets.push({
    x: -getRandom(target_model.width, 4 * canvas.width),
    y: getRandom(
      50 + target_model.height,
      canvas.height - 50 - target_model.height
    ),
    width: target_model.width,
    height: target_model.height,
    color: target_model.color,
    speed: getRandom(1, target_model.speed),
    direction: target_model.direction,
    image: target_model.image,
  });
}

function resettarget(i) {
  targets[i].x = -getRandom(canvas.width, canvas.width * 4);
  targets[i].y = getRandom(
    50 + target_model.height,
    canvas.height - 50 - target_model.height
  );
}

var keys = {
  ArrowRight: false,
  ArrowLeft: false,
  ArrowDown: false,
  ArrowUp: false,
  Space: false,
  KeyR: false,
};

function playerMovement() {
  if (keys.ArrowLeft) {
    if (player.moveleft) {
      player.x -= player.speed;
      player.moveright = 1;
    }
  }
  if (keys.ArrowRight) {
    if (player.moveright) {
      player.x += player.speed;
      player.moveleft = 1;
    }
  }

  if (keys.ArrowDown) {
    if (player.movedown) {
      player.y += player.speed;
      player.moveup = 1;
    }
  }
  if (keys.ArrowUp) {
    if (player.moveup) {
      player.y -= player.speed;
      player.movedown = 1;
    }
  }
  if (player.x <= 50) {
    player.moveleft = 0;
  }
  if (player.x >= canvas.width + player.width - 50) {
    player.moveright = 0;
  }
  if (player.y >= canvas.height - 50) {
    player.movedown = 0;
  }
  if (player.y <= 50) {
    player.moveup = 0;
  }
  for (let i = 0; i < targets.length; i++) {
    if (isRectCollision(targets[i], player)) {
      resettarget(i);
      player.health--;
    }
  }
}

function bullet_hit(bullet, target) {
  if (isRectCollision(bullet, target)) {
    target.x = -target.x;
    target.y = getRandom(50, 250);
    getRandom(target.speed, target.speed + 5);
    return true;
  }
}

var lastShotTime = 0;

function shoot(bullets, source, target) {
  if (keys.Space) {
    //? Create bullets
    const currentTime = Date.now();
    if (currentTime - lastShotTime >= player.cooldown * 1000) {
      var width;
      var height;
      if (source.direction == 1 || source.direction == 2) {
        width = bullet_model.height;
        height = bullet_model.width;
      } else {
        width = bullet_model.width;
        height = bullet_model.height;
      }

      const newBullet = {
        x: source.x + (source.width / 2 - width / 2),
        y: source.y + (source.height / 2 - height / 2),
        width: width,
        height: height,
        color: bullet_model.color,
        speed: bullet_model.speed,
        direction: source.direction,
      };
      bullets.push(newBullet);
      lastShotTime = currentTime; //* Update the last shot time
    }
  }

  //? Iterate over bullets in reverse order
  for (let i = bullets.length - 1; i >= 0; i--) {
    let hitTarget = false;

    //? Iterate over targets to check for collisions
    for (let j = 0; j < target.length; j++) {
      if (bullet_hit(bullets[i], target[j])) {
        hitTarget = true;
        resettarget(j);
        break; //* Break out of the inner loop once a collision is detected
      }
    }

    // If the bullet goes off the canvas or hits a target, remove it
    if (bullets[i].y < -bullets[i].height || hitTarget) {
      bullets.splice(i, 1);
    }
  }
  return bullets;
}

function animate(object) {
  if (Array.isArray(object)) {
    var animatedObjects = [];
    for (var i = 0; i < object.length; i++) {
      animatedObjects.push(animate(object[i]));
    }
    return animatedObjects;
  } else {
    switch (object.direction) {
      case 0:
        break;
      case 1: //left to right
        object.x += object.speed;
        break;
      case 2: //right to left
        object.x -= object.speed;
        break;
      case 3: //up to down
        object.y += object.speed;
        break;
      case 4: //down to up
        object.y -= object.speed;
        break;
    }
    return object;
  }
}

function render(object) {
  if (Array.isArray(object)) {
    for (var i = 0; i < object.length; i++) {
      render(object[i]);
    }
  } else {
    if (object.image instanceof Image) {
      ctx.drawImage(
        object.image,
        object.x,
        object.y,
        object.width,
        object.height
      );
    } else {
      ctx.fillStyle = object.color;
      ctx.fillRect(object.x, object.y, object.width, object.height);
    }
  }
}

function parallax(image, xPos = 0, speed) {
  const canvasWidth = ctx.canvas.width;
  const canvasHeight = ctx.canvas.height;

  // Calculate the scale factor to maintain the original aspect ratio
  const scale = canvasHeight / image.height;

  // Calculate the width of the repeated image
  const repeatedWidth = image.width * scale;

  // Calculate the total width covered by repeated images
  const totalWidth = repeatedWidth;

  // Calculate the source x position to create the illusion of movement
  let sourceX = (xPos * speed) % repeatedWidth;

  // Adjust sourceX for negative xPos values
  if (sourceX < 0) {
    sourceX += repeatedWidth;
  }

  // Draw repeated images horizontally to cover the entire canvas
  for (let x = -sourceX; x < canvasWidth; x += repeatedWidth) {
    ctx.drawImage(
      image,
      0,
      0,
      image.width,
      image.height,
      x,
      0,
      repeatedWidth,
      canvasHeight
    );
  }
}

function main() {
  for (var i = 0; i < targets.length; i++) {
    if (targets[i].x > canvas.width) {
      resettarget(i);
    }
  }

  if (player.health > 0) {
    playerMovement();
    bullets = animate(shoot(bullets, player, targets));
    targets = animate(targets);
    var seconds = performance.now() / 1000;
  }

  if (keys.KeyR) {
    player.health = max_health;
    for (var i = 0; i < targets.length; i++) {
      resettarget(i);
    }
    bullets = [];
  }

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  //? renders parallax
  parallax(background, seconds, -40);
  //? renders everything else
  render([bullets, player, targets]); //! leftmost will be drawn first

  ctx.fillStyle = "white";
  ctx.font = "50px Serif";
  if (player.health <= 0) {
    ctx.fillText("Game Over", 10, 50);
    ctx.font = "20px Serif";
    ctx.fillText("Press r to restart", canvas.width - 150, 50);
  } else {
    for (let i = 0; i < player.health; i++) {
      ctx.fillText("I", 10 + i * 20, 50);
    }
  }

  requestAnimationFrame(main);
}

document.addEventListener("keydown", function (evt) {
  if (evt.code in keys) {
    keys[evt.code] = true;
  }
});

document.addEventListener("keyup", function (evt) {
  if (evt.code in keys) {
    keys[evt.code] = false;
  }
});

background.onload = function () {
  requestAnimationFrame(main);
};
