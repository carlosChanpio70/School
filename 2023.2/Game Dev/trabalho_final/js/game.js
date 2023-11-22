import * as me from "https://esm.run/melonjs";

export default class Game {
  static updateAll(clickedBlock, click) {
    const blocks = me.game.world.getChildByName("block");
    var block;
    if (!me.state.current().gameover) {
      for (let i = 0; i < blocks.length; i++) {
        if (blocks[i] !== clickedBlock) continue;
        block = blocks[i];

        if (click.button == 0) {
          Game.handleLeftClick(block, blocks);
        }

        if (click.button == 2 && !block.isrevealed) {
          Game.handleRightClick(block);
        }

        break;
      }

      me.game.repaint();
    }
  }

  static handleLeftClick(block, blocks) {
    block.isrevealed = true;
    if (block.renderable.current?.name != "frame3") {
      if (block.isbomb) {
        Game.revealAllBombs(blocks, block);
      } else {
        Game.update(block, blocks);
      }
    }
  }

  static handleRightClick(block, blocks) {
    const frameName = block.renderable.current?.name;

    if (frameName == "frame3") {
      block.renderable.setCurrentAnimation("frame1");
      me.state.current().flags--;
    } else if (frameName == "frame1") {
      block.renderable.setCurrentAnimation("frame3");
      me.state.current().flags++;
    }

    var display1 = me.game.world.getChildByName("display1")[0];
    display1.setNumber(me.state.current().bombs - me.state.current().flags);
  }

  static revealAllBombs(blocks, block) {
    for (let i = 0; i < blocks.length; i++) {
      let b = blocks[i];
      if (b.isbomb) b.renderable.setCurrentAnimation("frame6");
    }
    block.renderable.setCurrentAnimation("frame7");
    me.state.current().gameover = true;
  }

  static update(block, blocks) {
    const bombs = block.getBombs();
    if (block.renderable.current?.name != "frame1") {
      var currentNumber =
        parseInt(block.renderable.current?.name.replace("frame", "")) - 8;
      var flagcount = 0;

      block.getNeighborBlocks();

      for (let i = 0; i < block.neighborBlocks.length; i++) {
        if (block.neighborBlocks[i].renderable.current?.name == "frame3") {
          flagcount++;
        }
      }

      if (currentNumber == flagcount) {
        Game.revealNeighboringBlocks(block, blocks);
      }
      return;
    }

    block.getNeighborBlocks();
    block.renderable.setCurrentAnimation("frame2");

    if (bombs) {
      Game.showNumber(block, bombs);
    } else {
      Game.revealNeighboringBlocks(block, blocks);
    }
  }

  static showNumber(block, bombs) {
    block.renderable.setCurrentAnimation(`frame${bombs + 8}`);
    me.state.current().revealedBlocksCount++;
  }

  static revealNeighboringBlocks(block, blocks) {
    block.neighborBlocks.forEach((b) => {
      if (!b.isrevealed) {
        b.isrevealed = true;
        Game.handleLeftClick(b, blocks);
        me.state.current().revealedBlocksCount++;
      }
    });
  }
}
