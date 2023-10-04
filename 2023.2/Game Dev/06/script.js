var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

var imgSonic = new Image();
var imgBackground = new Image();
imgSonic.src = "spritesheet.png";
imgBackground.src = "background.png";

// Passo estes valores conforme a minha spritesheet
var linhas = 3;
var colunas = 8;

// Dimensão de cada quadro
var largura = imgSonic.width / colunas;
var altura = imgSonic.height / linhas;

var selected_coluna = 0;
var selected_linha = 1;

var start_y = 300;
const player = {
  x: canvas.width / 2,
  y: start_y,
  width: 20,
  height: 20,
  speed: 5,
  x_acceleration: 0,
  y_acceleration: 0,
  moveleft: 1,
  moveright: 1,
  moveup: 1,
  movedown: 1,
  previousdirection: 0,
};

var keys = {
  ArrowRight: false,
  ArrowLeft: false,
  ArrowDown: false,
  ArrowUp: false,
  Space: false,
};

var pastTime = 0;

function movement() {
  var acceleration = 1; //Player's acceleration
  var friction = 1.2; //Player's friction
  var jump = 5 + (Math.abs(player.x_acceleration)/2);
  if (Math.abs(player.x_acceleration) <= player.speed || keys.Space) {
    if (keys.ArrowLeft) {
      player.x_acceleration -= acceleration;
    }
    if (keys.ArrowRight) {
      player.x_acceleration += acceleration;
    }
    if (keys.Space && player.y == start_y) {
      player.y_acceleration += jump;
    }
  }

  player.x += player.x_acceleration;
  player.y -= player.y_acceleration;
  if (player.x_acceleration != 0) {
    player.x_acceleration = player.x_acceleration / friction;
    if (Math.abs(player.x_acceleration) < 0.01) {
      player.x_acceleration = 0;
    }
  }
  if (player.y < start_y) {
    player.y_acceleration -= .25;
  }
  if (player.y >= start_y) {
    player.y_acceleration = 0;
    player.y = start_y;
  }
}

function animate() {
  const Delay = 50 / Math.abs(player.x_acceleration) + 50;
  var currentTime = Date.now();
  if (currentTime - pastTime >= Delay) {
    if (player.x_acceleration < 0) {
      selected_linha = 2;
      player.previousdirection = 1;
    }
    if (player.x_acceleration > 0) {
      selected_linha = 1;
      player.previousdirection = 0;
    }
    selected_coluna++;
    if (selected_coluna >= colunas) {
      selected_coluna = 0;
    }
    pastTime = currentTime;
  }
  if (Math.abs(player.x_acceleration) < 0.1) {
    selected_linha = 0;
    if (player.previousdirection) {
      selected_coluna = 1;
    } else {
      selected_coluna = 0;
    }
  }
}

function parallax(image,x,line) {
  var parallax_x = player.x/(x*4);
  var bgWidth = image.width;
  var bgHeight = image.height/4;

  // Calculate the number of times the image needs to be drawn to cover the canvas
  var repeats = Math.ceil(canvas.width / bgWidth)*2 + 1;

  for (var i = 0; i < repeats; i++) {
    // Calculate the x-coordinate for this repeat
    var drawX = (i * bgWidth*4) - (parallax_x % bgWidth*4)-canvas.width;

    context.drawImage(
      image,
      0,
      bgHeight*line,
      bgWidth,
      bgHeight,
      drawX,
      ((-player.y)+start_y)/x,
      bgWidth*4,
      canvas.height+x
    );
  }
}

function main() {
  movement();
  animate();

  // Posição de recorte
  var x = largura * selected_coluna;
  var y = altura * selected_linha;

  // Desenhando no Canvas

  context.clearRect(0, 0, canvas.width, canvas.height);
  parallax(imgBackground, 32, 0)
  parallax(imgBackground, 16, 1)  
  parallax(imgBackground, 8, 2)  
  parallax(imgBackground, 4, 3)  
  context.drawImage(
    imgSonic,
    x,
    y,
    largura,
    altura,
    canvas.width / 2,
    start_y,
    largura,
    altura
  );
  context.fillRect(
    0,
    (start_y+altura)+(start_y-player.y),
    canvas.width,
    canvas.height - start_y
  )

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

imgSonic.onload = function () {
  main();
};
