var canvas = document.getElementById('canvas');
var context = canvas.getContext("2d");

var img = new Image();
img.src = 'spritesheet.png';

// Passo estes valores conforme a minha spritesheet
var linhas = 4;
var colunas = 6;

// Dimensão de cada quadro
var largura = img.width / colunas;
var altura = img.height / linhas;

var pastTime = 0;
const Delay = 35;

var selected_coluna = 0;
var selected_linha = 1;

const player = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    width: 20, height: 20, color: "black", speed: 5,
    moveleft: 1,
    moveright: 1,
    moveup: 1,
    movedown: 1,
    previousdirection: 0
};

var keys = {
    ArrowRight: false,
    ArrowLeft: false,
    ArrowDown: false,
    ArrowUp: false,
    Space: false
};

function movement() {
    var currentTime = Date.now();
    if (keys.ArrowLeft || keys.ArrowRight || keys.ArrowUp || keys.ArrowDown) {
        if (keys.ArrowLeft) {
            player.x -= player.speed
            selected_linha = 1
            if (currentTime - pastTime >= Delay) {
                selected_coluna++;
                if (selected_coluna >= colunas) {
                    selected_coluna = 0;
                }
                pastTime = currentTime;
            }
            player.previousdirection = 1
        }
        if (keys.ArrowRight) {
            player.x += player.speed
            selected_linha = 2
            if (currentTime - pastTime >= Delay) {
                selected_coluna++;
                if (selected_coluna >= colunas) {
                    selected_coluna = 0;
                }
                pastTime = currentTime;
            }
            player.previousdirection = 2
        }
        if (keys.ArrowUp) {
            player.y -= player.speed
            selected_linha = 3
            if (currentTime - pastTime >= Delay) {
                selected_coluna++;
                if (selected_coluna >= colunas) {
                    selected_coluna = 0;
                }
                pastTime = currentTime;
            }
            player.previousdirection = 3
        }
        if (keys.ArrowDown) {
            player.y += player.speed
            selected_linha = 0
            if (currentTime - pastTime >= Delay) {
                selected_coluna++;
                if (selected_coluna >= colunas) {
                    selected_coluna = 0;
                }
                pastTime = currentTime;
            }
            player.previousdirection = 0
        }
    } else {
        selected_coluna = 5;
        selected_linha = player.previousdirection;
    }
}

function main() {
    movement()

    // Posição de recorte
    var x = largura * selected_coluna;
    var y = altura * selected_linha;

    // Desenhando no Canvas
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, x, y, largura, altura, player.x, player.y, largura, altura);

    requestAnimationFrame(main);
}

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

img.onload = function () { main(); }