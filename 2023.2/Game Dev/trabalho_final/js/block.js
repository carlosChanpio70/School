import * as me from "https://esm.run/melonjs";

// Define the Block entity class
export default class Block extends me.Entity {
  constructor(x, y, isbomb, update) {
    super(x, y, {
      width: 16,
      height: 16,
    });

    this.isrevealed = false;
    this.isbomb = isbomb;
    this.anchorPoint.set(0.5, 0.5);

    this.renderable = new me.Sprite(0, 0, {
      image: me.loader.getImage("block"),
      framewidth: 16,
      frameheight: 16,
    });
    for (let i = 1; i <= 16; i++) {
      this.renderable.addAnimation(`frame${i}`, [i - 1]);
    }

    this.renderable.setCurrentAnimation("frame1"); // default frame

    me.input.registerPointerEvent("pointerdown", this, (event) => {
      if (
        event.gameX > this.pos.x &&
        event.gameX < this.pos.x + this.width &&
        event.gameY > this.pos.y &&
        event.gameY < this.pos.y + this.height
      ) {
        update(this, event);
      }
    });
  }
  setFrame(frame_n) {
    this.renderable.setCurrentAnimation(`frame${frame_n}`);
  }

  reset(bomb) {
    this.isrevealed = false;
    this.isbomb = bomb;
    this.renderable.setCurrentAnimation("frame1");
    this.neighborBlocks = [];
  }

  getBombs() {
    var n = 0;
    this.getNeighborBlocks();
    for (let i = 0; i < this.neighborBlocks.length; i++) {
      if (this.neighborBlocks[i].isbomb == 1) {
        n++;
      }
    }
    return n;
  }

  getNeighborBlocks() {
    this.neighborBlocks = [];
    var blocks = me.game.world.getChildByName("block");

    for (let i = 0; i < blocks.length; i++) {
      const block = blocks[i];

      if (block !== this && this.isNeighborBlock(block)) {
        this.neighborBlocks.push(block);
      }
    }
  }

  isNeighborBlock(block) {
    const dx = Math.abs(block.pos.x - this.pos.x);
    const dy = Math.abs(block.pos.y - this.pos.y);

    // Check if the block is within the 3x3 grid centered around the current block
    return dx <= this.width && dy <= this.height;
  }
}
