import * as me from "https://esm.run/melonjs";
import Block from "./block.js";
import Game from "./game.js";
import PlayButton from "./reset.js";
import Display from "./display.js";

export default class PlayStage extends me.Stage {
  constructor() {
    super();

    this.width = 20;
    this.height = 20;
    this.bombs = 60;
    this.revealedBlocksCount = 0;
    this.flags = 0;
    this.border = 5;
    this.header = 48;
    this.gameover = false;
    this.startTime = null;
  }

  updateDisplay2() {
    var display2 = me.game.world.getChildByName("display2")[0];
    display2.setNumber(
      Math.floor((me.timer.getTime() - this.startTime) / 1000)
    );
  }

  randomizeBombs() {
    // Initialize all coordinates to false
    var bombs_coords = Array(this.width * this.height).fill(false);

    // Place the bombs randomly in the coordinates
    var shuffled_indexes = Array.from(
      { length: this.width * this.height },
      (_, i) => i
    ).sort(() => Math.random() - 0.5);
    for (let i = 0; i < this.bombs; i++) {
      bombs_coords[shuffled_indexes[i]] = true;
    }

    return bombs_coords;
  }

  resetBlocks() {
    this.gameover = false;
    // Get all existing blocks
    const blocks = me.game.world.getChildByName("block");

    // Generate new randomized bomb locations
    var bombs_coords = this.randomizeBombs();

    // Update blocks setting them as bombs based on randomized bomb locations
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        blocks[j * this.width + i].reset(bombs_coords[j * this.width + i]);
      }
    }
    this.startTime = me.timer.getTime();
    var display1 = me.game.world.getChildByName("display1")[0];
    display1.setNumber(this.bombs);
  }

  onResetEvent() {
    var colorLayer = new me.ColorLayer("background", "#c0c0c0", 0);
    me.game.world.addChild(colorLayer, 0);

      // Add the blocks to the game world
    var x = this.width;
    var y = this.height;
    var bombs = this.bombs;

    var bombs_coords = this.randomizeBombs(x, y, bombs);

    // Create new block objects and add them to the game world
    for (let i = 0; i < x; i++) {
      for (let j = 0; j < y; j++) {
        var block = new Block(
          i * 16 + this.border,
          j * 16 + this.header,
          bombs_coords[j * x + i], // Fixed the indexing here
          Game.updateAll.bind(this)
        );
        block.name = "block";
        me.game.world.addChild(block);
      }
    }

    var reset = new PlayButton(
      (this.width * 16+ this.border) / 2 + 10,
      this.header / 2,
      this
    );
    reset.name = "play";
    me.game.world.addChild(reset);

    var display1 = new Display(
        (this.width * 16+ this.border) / 8,
      this.header / 2
    );
    display1.name = "display1";
    display1.setNumber(this.bombs);
    me.game.world.addChild(display1);

    var display2 = new Display(
      (this.width * 16+ this.border )* 7 / 8 - 13,
      this.header / 2
    );
    display2.name = "display2";
    me.game.world.addChild(display2);

    this.startTime = me.timer.getTime();
    me.timer.setInterval(this.updateDisplay2.bind(this), 10);
  }
}
