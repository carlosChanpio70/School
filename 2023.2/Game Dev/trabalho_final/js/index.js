import * as me from "https://esm.run/melonjs";
import PlayStage from "./stage.js"

export default function onload() {
  var stage = new PlayStage();
  if (!me.video.init(stage.width * 16 + 2 * stage.border, stage.height * 16 + stage.header + stage.border, { wrapper: "screen", scale: "auto" })) {
    alert("Your browser does not support HTML5 canvas.");
    return;
  }

  // Disable gravity in the game world
  me.game.world.gravity.y = 0;

  // Set the Play stage
  me.state.set(me.state.PLAY, stage);

  // Start the game
  me.loader.preload(
    [
      { name: "block", type: "image", src: "./img/block.png" },
      { name: "numbers", type: "image", src: "./img/numbers.png" },
      { name: "status", type: "image", src: "./img/status.png" },
    ],
    function () {
      me.state.change(me.state.PLAY);
    }
  );
}