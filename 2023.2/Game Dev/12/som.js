function sound(src) {
  this.sound = null;
  this.play = function(){
      this.sound = document.createElement("audio");
      this.sound.src = src;
      this.sound.setAttribute("preload", "auto");
      this.sound.setAttribute("controls", "none");
      this.sound.style.display = "none";
      document.body.appendChild(this.sound);
      this.sound.play();
  }
  this.stop = function(){
      if(this.sound) {
          this.sound.pause();
      }
  }
}