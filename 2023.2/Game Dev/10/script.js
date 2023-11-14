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

function getDistance(point1, point2) {
  var dx = point2.x - point1.x;
  var dy = point2.y - point1.y;
  return Math.sqrt(dx * dx + dy * dy);
}

function CircleCollision(circle1, circle2) {
  const distanceX = circle1.x - circle2.x;
  const distanceY = circle1.y - circle2.y;
  const distanceBetweenCenters = Math.sqrt(
    distanceX * distanceX + distanceY * distanceY
  );

  if (distanceBetweenCenters < circle1.radius + circle2.radius) {
    circle1.hits++;
    circle2.hits++;
    const collisionAngle = Math.atan2(distanceY, distanceX);

    const velocity1 = Math.hypot(circle1.x_velocity, circle1.y_velocity);
    const velocity2 = Math.hypot(circle2.x_velocity, circle2.y_velocity);
    const direction1 = Math.atan2(circle1.y_velocity, circle1.x_velocity);
    const direction2 = Math.atan2(circle2.y_velocity, circle2.x_velocity);

    const rotatedVelX1 = velocity1 * Math.cos(direction1 - collisionAngle);
    const rotatedVelY1 = velocity1 * Math.sin(direction1 - collisionAngle);
    const rotatedVelX2 = velocity2 * Math.cos(direction2 - collisionAngle);
    const rotatedVelY2 = velocity2 * Math.sin(direction2 - collisionAngle);

    const finalVelocityX1 =
      ((circle1.radius - circle2.radius) * rotatedVelX1 +
        2 * circle2.radius * rotatedVelX2) /
      (circle1.radius + circle2.radius);
    const finalVelocityX2 =
      (2 * circle1.radius * rotatedVelX1 +
        (circle2.radius - circle1.radius) * rotatedVelX2) /
      (circle1.radius + circle2.radius);

    const cosineAngle = Math.cos(collisionAngle);
    const sineAngle = Math.sin(collisionAngle);
    const cosinePerpendicular = Math.cos(collisionAngle + Math.PI / 2);
    const sinePerpendicular = Math.sin(collisionAngle + Math.PI / 2);

    circle1.x_velocity =
      cosineAngle * finalVelocityX1 + cosinePerpendicular * rotatedVelY1;
    circle1.y_velocity =
      sineAngle * finalVelocityX1 + sinePerpendicular * rotatedVelY1;
    circle2.x_velocity =
      cosineAngle * finalVelocityX2 + cosinePerpendicular * rotatedVelY2;
    circle2.y_velocity =
      sineAngle * finalVelocityX2 + sinePerpendicular * rotatedVelY2;
  }
  return [circle1, circle2];
}

var mousePosition = { x: 0, y: 0 };
canvas.onmousemove = function (event) {
  mousePosition.x = event.clientX;
  mousePosition.y = event.clientY;
};

let circles = [];

var circles_amount = 10;
var circle_radius = 20;
var speed = 5;
for (var i = 0; i < circles_amount; i++) {
  const circle = {
    x: ((canvas.width - circle_radius) / circles_amount) * i + circle_radius,
    y: 50,
    x_velocity: getRandom(-speed, speed),
    y_velocity: getRandom(-speed, speed),
    radius: circle_radius,
    color: "black",
    hits: 0,
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

      for (var j = i + 1; j < object.length; j++) {
        var results = CircleCollision(object[i], object[j]);
        object[i] = results[0];
        object[j] = results[1];
      }

      var max_hits = 3 //max number of hits before dissapearence
      object[i].color = `rgb(${object[i].hits * ((1 / max_hits) * 255)},0,0)`;
      if (object[i].hits >= max_hits+1) {
        object.splice(i,1)
      }
    }
    pastTime = currentTime;
    return object;
  }
  return object;
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

var intervalId;

canvas.onmousedown = function(event) {
  intervalId = setInterval(function() {
    var attraction_a = 5;
    for (var i = 0; i < circles.length; i++) {
      var distance = getDistance(circles[i], mousePosition);
      if (circles[i].x >= mousePosition.x) {
        circles[i].x_velocity -= attraction_a/Math.abs(distance);
      } else {
        circles[i].x_velocity += attraction_a/Math.abs(distance);
      }
      if (circles[i].y >= mousePosition.y) {
        circles[i].y_velocity -= attraction_a/Math.abs(distance);
      } else {
        circles[i].y_velocity += attraction_a/Math.abs(distance);
      }
    }
  }, 10); // Modify this number to change the frequency of execution
};


canvas.onmouseup = function() {
  clearInterval(intervalId);
};

requestAnimationFrame(main);
