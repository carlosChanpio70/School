var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var color = "black";
var score = 0;
var bullets = [];
var targets = [];

//Return random number between 2 numbers
function getRandom(n0, n1) {
  var n2 = n1;
  if (n0 > n1) {
    n1 = n0;
    n0 = n2;
  }
  return Math.floor(Math.random() * (n1 - n0)) + n0;
}

//Check collision between 2 objects
function isRectCollision(rect1, rect2) {
  return (
    rect1.x < rect2.x + rect2.width &&
    rect1.x + rect1.width > rect2.x &&
    rect1.y < rect2.y + rect2.height &&
    rect1.y + rect1.height > rect2.y
  );
}

const player = {
  x: canvas.width / 2,
  y: canvas.height - 75,
  width: 20,
  height: 20,
  color: color,
  speed: 5,
  moveleft: 1,
  moveright: 1,
  moveup: 1,
  movedown: 1,
  direction: 4,
};
const target_model = {
  x: canvas.width / 2,
  y: 0,
  width: 20,
  height: 5,
  color: color,
  speed: 2,
  direction: 1,
};
const bullet_model = {
  x: -10,
  y: 0,
  width: 5,
  height: 20,
  color: color,
  speed: 10,
};

for (var i = 0; i < 0; i++) {
  targets.push({
    x: -getRandom(0, target_model.speed * 2 * canvas.width),
    y: getRandom(50, 250),
    width: target_model.width,
    height: target_model.height,
    color: target_model.color,
    speed: getRandom(target_model.speed, target_model.speed + 5),
    direction: target_model.direction,
  });
}

var keys = {
  ArrowRight: false,
  ArrowLeft: false,
  ArrowDown: false,
  ArrowUp: false,
  Space: false,
};

function playerMovement() {
  if (keys.Space) {
    player.color = "red";
  } else {
    player.color = "black";
  }
  if (keys.ArrowLeft) {
    if (player.moveleft) {
      player.x -= player.speed;
      player.direction = 2;
      player.moveright = 1;
    }
  }
  if (keys.ArrowRight) {
    if (player.moveright) {
      player.x += player.speed;
      player.direction = 1;
      player.moveleft = 1;
    }
  }

  if (keys.ArrowDown) {
    if (player.movedown) {
      player.y += player.speed;
      player.direction = 3;
      player.moveup = 1;
    }
  }
  if (keys.ArrowUp) {
    if (player.moveup) {
      player.y -= player.speed;
      player.direction = 4;
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
}

var lastShotTime = 0;
const shotDelay = 250; // Delay in milliseconds

function bullet_hit(bullet, target) {
  if (isRectCollision(bullet, target)) {
    target.x = -target.x;
    target.y = getRandom(50, 250);
    getRandom(target.speed, target.speed + 5);
    score++;
    return true;
  }
}

function shoot(bullets, source, target) {
  if (keys.Space) {
    //Create bullets
    const currentTime = Date.now();
    if (currentTime - lastShotTime >= shotDelay) {
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
      lastShotTime = currentTime; // Update the last shot time
    }
  }

  // Iterate over bullets in reverse order
  for (let i = bullets.length - 1; i >= 0; i--) {
    let hitTarget = false;

    if (Array.isArray(target)) {
      // Iterate over targets to check for collisions
      for (let j = 0; j < target.length; j++) {
        if (bullet_hit(bullets[i], target[j])) {
          hitTarget = true;
          break; // Break out of the inner loop once a collision is detected
        }
      }
    } else {
      if (bullet_hit(bullets[i], target)) {
        hitTarget = true;
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
    context.fillStyle = object.color;
    context.fillRect(object.x, object.y, object.width, object.height);
  }
}

function main() {
  playerMovement();

  for (var i = 0; i < targets.length; i++) {
    if (targets[i].x > canvas.width) {
      targets[i].x = -(targets[i].speed * canvas.width);
    }
  }

  bullets = animate(shoot(bullets, player, targets));
  targets = animate(targets);

  context.clearRect(0, 0, canvas.width, canvas.height);

  render([bullets,player, targets]);//leftmost will be drawn first

  context.fillStyle = "black";
  context.font = "50px Serif";
  context.fillText(score, 10, 50);

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

requestAnimationFrame(main);
