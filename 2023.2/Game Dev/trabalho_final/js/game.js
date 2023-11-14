import * as me from "https://esm.run/melonjs";

export default class Game {
    static updateAll(clickedBlock, click) {
      const blocks = me.game.world.getChildByName("block");
      var block;
      for (let i = 0; i < blocks.length; i++) {
        if (blocks[i] !== clickedBlock) continue;
        block = blocks[i];
  
        if (click.button == 0)
        Game.handleLeftClick(block, blocks);
  
        if (click.button == 2 && !block.isrevealed)
        Game.handleRightClick(block);
  
        break;
      }
      me.game.repaint();
    }
  
    static handleLeftClick(block, blocks) {
      block.isrevealed = true;
      if (block.isbomb)
      Game.revealAllBombs(blocks, block);
      else
      Game.update(block);
    }
  
    static revealAllBombs(blocks, block) {
      blocks.forEach(b => {
        if (b.isbomb)
          b.renderable.setCurrentAnimation("frame6");
      });
      block.renderable.setCurrentAnimation("frame7");
    }
  
    static handleRightClick(block) {
      const frameName = block.renderable.current?.name;
  
      if (frameName == "frame3")
        block.renderable.setCurrentAnimation("frame1");
      else if (frameName == "frame1")
        block.renderable.setCurrentAnimation("frame3");
    }
  
    static update(block) {
      const bombs = block.getBombs();
  
      if (!block.isrevealed)
        return;
  
      block.getNeighborBlocks();
      block.renderable.setCurrentAnimation("frame2");
  
      if (bombs)
      Game.revealBombs(block, bombs);
      else
      Game.revealNeighboringBlocks(block);
    }
  
    static revealBombs(block, bombs) {
      block.renderable.setCurrentAnimation(`frame${bombs + 8}`);
      me.state.current().revealedBlocksCount++;
    }
  
    static revealNeighboringBlocks(block) {
      block.neighborBlocks.forEach(b => {
        if (!b.isrevealed) {
          b.isrevealed = true;
          Game.update(b);
          me.state.current().revealedBlocksCount++;
        }
      });
    }
  } 