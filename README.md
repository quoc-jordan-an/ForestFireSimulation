# ForestFireSimulation
This is an extra credit problem in my CS class. I think it's cool, so I put it up here.
The program animated the generation of a forest from barren to burned if you set some number of spots on fire randomly.
Each cell in the grid will be in one of five states: Barren, DryGrass, Fire,  HotFire, Burned.
The rules for updating the generations are:
1. If a DryGrass cell has a neighbor which is Fire or HotFire, the cell becomes HotFire in the next generation, otherwise it stays DryGrass.
2. If a Barren cell has a neighbor which is HotFire, the cell becomes Fire in the next generation, otherwise it stays Barren.
3. A HotFire cell always becomes a Fire cell in the next generation.
4. If a Fire cell has a neighbor which is HotFire, the cell says Fire in the next generation, otherwise it becomes Burned.
5. A Burned cell always stays Burned.
