import * as me from "https://esm.run/melonjs";

export default class Display extends me.Container {
  constructor(x, y) {
    super(x, y, {
      width: 39,
      height: 23,
    });
    this.anchorPoint.set(0.5, 0.5);

    this.renderables = [];
    for (let i = 0; i < 3; i++) {
      this.renderables[i] = new me.Sprite(i * 13, 0, {
        image: me.loader.getImage("numbers"),
        framewidth: 13,
        frameheight: 23,
      });

      // Set up the animations
      for (let j = 1; j < 10; j++) {
        this.renderables[i].addAnimation(`frame${j}`, [j - 1]);
      }

      // Add frame0 animation
      this.renderables[i].addAnimation(`frame0`, [9]);

      this.renderables[i].setCurrentAnimation(`frame0`);

      // Add each sprite as a separate entity to the game world
      this.addChild(this.renderables[i]);
    }
  }

  setNumber(num) {
    let hundreds = Math.floor(num / 100);
    let tens = Math.floor((num % 100) / 10);
    let ones = num % 10;

    this.renderables[0].setCurrentAnimation(`frame${hundreds}`);
    this.renderables[1].setCurrentAnimation(`frame${tens}`);
    this.renderables[2].setCurrentAnimation(`frame${ones}`);
    me.game.repaint();
  }
}
