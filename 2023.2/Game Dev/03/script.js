var keys = {
  ArrowRight: false,
  ArrowLeft: false,
  ArrowDown: false,
  ArrowUp: false,
  Space: false,
};

function Animacao(context) {
  this.context = context;
  this.sprites = [];
  this.ligado = false;
}

Animacao.prototype = {
  novoSprite: function (sprite) {
    this.sprites.push(sprite);
  },
  ligar: function () {
    this.ligado = true;
    this.proximoFrame();
  },
  desligar: function () {
    this.ligado = false;
  },
  proximoFrame: function () {
    if (keys.Space && this.ligado) {
      this.desligar()
    }

    // Posso continuar?
    if (!this.ligado) return;
    

    // A cada ciclo, limpamos a tela ou desenhamos um fundo
    this.limparTela();

    // Atualizamos o estado dos sprites
    for (var i in this.sprites) this.sprites[i].atualizar();

    // Desenhamos os sprites
    for (var i in this.sprites) this.sprites[i].desenhar();

    // Chamamos o próximo ciclo
    var animacao = this;
    requestAnimationFrame(function () {
      animacao.proximoFrame();
    });
  },
  limparTela: function () {
    var ctx = this.context;
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  },
};

function Bola(context) {
  this.context = context;
  this.x = 0;
  this.y = 0;
  this.velocidadeX = 0;
  this.velocidadeY = 0;

  // Atributos de desenho padrão
  this.cor = "black";
  this.img = 0;
  this.width = 0;
  this.heigh = 0;
  this.linha = 0;
  this.coluna = 0;
  this.raio = 10;
}

Bola.prototype = {
  atualizar: function () {
    var ctx = this.context;

    if (this.x < this.raio || this.x > ctx.canvas.width - this.raio)
      this.velocidadeX *= -1;

    if (this.y < this.raio || this.y > ctx.canvas.height - this.raio)
      this.velocidadeY *= -1;

    this.x += this.velocidadeX;
    this.y += this.velocidadeY;
  },
  desenhar: function () {
    var ctx = this.context;

    // Guardar configurações atuais do contexto
    ctx.save();

    // Configurar o contexto de acordo com a bola
    ctx.fillStyle = this.cor;

    // Desenhar
    if (this.img == 0) {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.raio, 0, 2 * Math.PI, false);
      ctx.fill();
    } else {
      ctx.drawImage(
        this.img,
        this.width * this.coluna,
        this.height * this.linha,
        this.width,
        this.heigh,
        this.x,
        this.y,
        this.raio * 2,
        this.raio * 2
      );
    }

    // Voltar às configurações anteriores
    ctx.restore();
  },
};

var image = new Image();
image.src = "img/bolas.png";
var showimg = 0; //Mude isso para 1 para mostrar sprites

// Referências para o Canvas
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

// Criando alguns sprites
var b1 = new Bola(context);
b1.x = 100;
b1.y = 200;
b1.velocidadeX = 2.5;
b1.velocidadeY = -5;
b1.cor = "red";
b1.raio = 30;

var b2 = new Bola(context);
b2.x = 200;
b2.y = 100;
b2.velocidadeX = -5;
b2.velocidadeY = 2.5;
b2.cor = "blue";
b2.raio = 25;

var b3 = new Bola(context);
b3.x = 300;
b3.y = 200;
b3.velocidadeX = 5;
b3.velocidadeY = -2.5;
b3.cor = "black";
b3.raio = 25;

var b4 = new Bola(context);
b4.x = 200;
b4.y = 300;
b4.velocidadeX = 5;
b4.velocidadeY = -5;
b4.cor = "green";
b4.raio = 20;

var width = image.width / 4;
var heigh = image.height / 3;
if (showimg) {
  b1.width = width;
  b1.heigh = heigh;
  b2.width = width;
  b2.heigh = heigh;
  b3.width = width;
  b3.heigh = heigh;
  b4.width = width;
  b4.heigh = heigh;
  b1.img = image;
  b2.img = image;
  b3.img = image;
  b4.img = image;
  b1.coluna = 1;
  b1.linha = 1;
  b2.coluna = 1;
  b2.linha = 1;
  b3.coluna = 1;
  b3.linha = 1;
  b4.coluna = 1;
  b4.linha = 1;
}
// Criando o loop de animação
var animacao = new Animacao(context);
animacao.novoSprite(b1);
animacao.novoSprite(b2);
animacao.novoSprite(b3);
animacao.novoSprite(b4);

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

image.onload = function () {
  animacao.ligar(); // "Ligar" a animação
};
