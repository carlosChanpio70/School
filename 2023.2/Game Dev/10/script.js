var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

function getRandom(n0, n1) {
  var n2 = n1;
  if (n0 > n1) {
    n1 = n0;
    n0 = n2;
  }
  return Math.floor(Math.random() * (n1 - n0)) + n0;
}

function getDistance(n0, n1) {
  var dx = n1.x - n0.x;
  var dy = n1.y - n0.y;
  return (Math.sqrt(dx * dx + dy * dy));
}

function CircleCollision(circle1, circle2) {
  if (getDistance(circle1,circle2) < circle1.radius + circle2.radius) {
    // Calculate the angle of collision
    var angle = Math.atan2(dy, dx);

    // Calculate the new velocities using trigonometry
    var speed1 = Math.sqrt(circle1.x_velocity^2 + circle1.y_velocity^2);
    var speed2 = Math.sqrt(circle2.x_velocity^2 + circle2.y_velocity^2);

    var direction1 = Math.atan2(circle1.y_velocity, circle1.x_velocity);
    var direction2 = Math.atan2(circle2.y_velocity, circle2.x_velocity);

    // Swap the velocities after the collision
    circle1.x_velocity = speed2 * Math.cos(direction2 - angle);
    circle1.y_velocity = speed2 * Math.sin(direction2 - angle);
    circle2.x_velocity = speed1 * Math.cos(direction1 - angle);
    circle2.y_velocity = speed1 * Math.sin(direction1 - angle);
  }
  return [circle1, circle2];
}

let circles = [];
for (var i = 0; i < 5; i++) {
  const circle = {
    x: 50*i+50,
    y: 50,
    x_velocity: getRandom(-5, 5),
    y_velocity: getRandom(-5, 5),
    radius: 10,
    color: `rgb(${i*50},0,0)`,
  };
  circles.push(circle);
}

var Delay = 20;
var pastTime = 0;
function animate(object) {
  var currentTime = Date.now();
  if (currentTime - pastTime >= Delay) {
    for (var i = 0; i < object.length; i++) {
      object[i].x += object[i].x_velocity;
      object[i].y += object[i].y_velocity;

      if (
        object[i].x > canvas.width - object[i].radius ||
        object[i].x < 0 + object[i].radius
      ) {
        object[i].x_velocity *= -1;
      }
      if (
        object[i].y > canvas.height - object[i].radius ||
        object[i].y < 0 + object[i].radius
      ) {
        object[i].y_velocity *= -1;
      }

      for (var j = i+1; j < object.length; j++) {
        var results = CircleCollision(object[i], object[j])
        object[i] = results[0];
        object[j] = results[1];
      }
    }
    pastTime = currentTime;
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
    context.beginPath();
    context.arc(object.x, object.y, object.radius, 0, 2 * Math.PI, false);
    context.fill();
  }
}

function main() {
  context.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

  circles = animate(circles);
  render(circles);

  requestAnimationFrame(main);
}

requestAnimationFrame(main);
