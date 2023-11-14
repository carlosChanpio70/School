import * as me from "https://esm.run/melonjs";
import Block from "./block.js";
import Game from "./game.js";

// Define the Play stage
class PlayStage extends me.Stage {
  constructor() {
    super();

    this.width = 20;
    this.height = 20;
    this.bombs = 40;
    this.revealedBlocksCount = 0;
  }
  onResetEvent() {
    var x = this.width;
    var y = this.height;
    var bombs = this.bombs;

    var bombs_coords = Array(x * y).fill(false);
    for (let i = 0; i < bombs; i++) {
      bombs_coords[i] = true;
    }
    bombs_coords = bombs_coords.sort(() => Math.random() - 0.5);

    for (let j = 0; j < x; j++) {
      for (let i = 0; i < y; i++) {
        var block = new Block(
          j * 16 + 5,
          i * 16 + 40,
          bombs_coords[j * y + i],
          Game.updateAll.bind(this)
        );
        block.name = "block"; // Set the name of the block
        me.game.world.addChild(block);
      }
    }
  }
}

export default function onload() {
  if (!me.video.init(800, 600, { wrapper: "screen", scale: "auto" })) {
    alert("Your browser does not support HTML5 canvas.");
    return;
  }

  // Disable gravity in the game world
  me.game.world.gravity.y = 0;

  // Set the Play stage
  me.state.set(me.state.PLAY, new PlayStage());

  // Start the game
  me.loader.preload(
    [{ name: "block", type: "image", src: "./img/block.png" }],
    function () {
      me.state.change(me.state.PLAY);
    }
  );
}
