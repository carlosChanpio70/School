function Animacao(context) {
   this.context = context;
   this.sprites = [];
   this.ligado = false;
   this.spritesExcluir = []
}
Animacao.prototype = {
   novoSprite: function(sprite) {
      this.sprites.push(sprite);
      sprite.animacao = this;
   },
   ligar: function() {
      this.ligado = true;
      this.proximoFrame();
   },
   desligar: function() {
      this.ligado = false;
   },
   proximoFrame: function() {
      // Posso continuar?
      if ( ! this.ligado ) return;

      // A cada ciclo, limpamos a tela ou desenhamos um fundo
      this.limparTela();

      // Atualizamos o estado dos sprites
      for (var i in this.sprites)
         this.sprites[i].atualizar();

      // Desenhamos os sprites
      for (var i in this.sprites)
         this.sprites[i].desenhar();

      // Chamamos o próximo ciclo
      var animacao = this;
      requestAnimationFrame(function() {
         animacao.proximoFrame();
      });
   },
   limparTela: function() {
      var ctx = this.context;
      ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
   },
   excluirSprite: function(sprite) {
      this.spritesExcluir.push(sprite);
   },
   processarExclusoes: function() {
      // Criar um novo array
      var novoArray = [];
      
      // Adicionar somente os elementos não excluídos
      for (var i in this.sprites) {
         if (this.spritesExcluir.indexOf(this.sprites[i]) == -1)
            novoArray.push(this.sprites[i]);
      }
      
      // Limpar o array de exclusões
      this.spritesExcluir = [];
      
      // Substituir o array velho pelo novo
      this.sprites = novoArray;
   }
}
