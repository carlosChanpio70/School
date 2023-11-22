import * as me from "https://esm.run/melonjs";

export default class PlayButton extends me.Entity {
  constructor(x, y, PlayStage) {
    super(x - 12, y - 12, {
      width: 24,
      height: 24,
    });
    this.anchorPoint.set(0.5, 0.5);

    this.renderable = new me.Sprite(0, 0, {
      image: me.loader.getImage("status"),
      framewidth: 24,
      frameheight: 24,
    });

    for (let i = 1; i <= 16; i++) {
      this.renderable.addAnimation(`frame${i}`, [i - 1]);
    }

    this.renderable.setCurrentAnimation("frame1");

    me.input.registerPointerEvent("pointerdown", this, (event) => {
      if (
        event.gameX > this.pos.x &&
        event.gameX < this.pos.x + this.width &&
        event.gameY > this.pos.y &&
        event.gameY < this.pos.y + this.height
      ) {
        this.renderable.setCurrentAnimation("frame2");
        me.game.repaint();
      }
    });

    me.input.registerPointerEvent("pointerup", this, (event) => {
      if (
        event.gameX > this.pos.x &&
        event.gameX < this.pos.x + this.width &&
        event.gameY > this.pos.y &&
        event.gameY < this.pos.y + this.height
      ) {
        this.renderable.setCurrentAnimation("frame1");
        me.game.repaint();
        PlayStage.resetBlocks();
      }
    });

    setInterval(() => {
      if (me.state.current().gameover) {
        this.renderable.setCurrentAnimation("frame5");
      }
    }, 10);
  }
}
