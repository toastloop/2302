# DO NOT MODIFY EXISTING CODE - you may add helper classes if you deem necessary
import random
class Player:
    def __init__(self, name, tiles=None):
        self.name = name
        self.tiles = tiles if tiles is not None else {"red": [[], []],"blue": [[], []],"black": [[], []],"yellow": [[], []]}
        self.hasPlayedFirstMove = False
        self.errorMessages = ['Invalid Number of Tiles: Please select a valid number of tiles.',
            'Invalid Tiles: You passed in a tile or tiles that you do not currently have in your tiles set.',
            'Duplicate Tile: Duplicate tiles (tiles with the same number and color) in one tile set are not allowed.',
            'Invalid Move: Please make sure all your tiles add to at least 30.',
            'Invalid Sequence: please make sure that all numbers of the same color are in a sequence of +1 from each other, for example: 1,2,3 and not 1,2,4..',
            'Invalid Combination: please make sure that all numbers of different colors are the same number.']
    def printTiles(self): 
        print(self.name + "'s Tiles:")
        [print('\t{}:{}{}'.format(key, "\t", self.tiles[key])) for key in self.tiles]
    def addTileToPlayerTiles(self,color,number):
        self.sort(self.tiles[color][number in self.tiles[color][0]].append(number))
    def assignTiles(self,tilesDeck):
        [self.assignTile(tilesDeck) for i in range(14)]
    def assignTilesRec(self,tilesDeck,numOfTiles):
        return self.assignTilesRec(self.assignTile(tilesDeck),numOfTiles-1) if numOfTiles>0 else None
    def placeTileOnTable(self, color, number):
        return self.tiles[color][number in self.tiles[color][1]].remove(number) if any(number in sub for sub in self.tiles[color]) else print(self.errorMessages[1])
    def checkIfTileExists(self,color,number)->bool:
        return any(number in sub for sub in self.tiles[color])
    def checkDuplicateTiles(self,tiles)->bool:
        return len(set(list(zip(tiles[0::2],tiles[1::2]))))!=len(tiles[0::2])
    def areAllTilesSameColor(self,tiles)->bool:
        return len(set(tiles[0::2]))==1
    def areAllTilesSameColorRec(self,tiles,colorSet:set)->bool:
        return len(colorSet)==1 if len(tiles)<1 else self.areAllTilesSameColorRec(tiles[2:],colorSet|{tiles[0]}) 
    def getOnlyTileNumbersRec(self,tiles,tileNums:list)->list:
        return tileNums if len(tiles)==0 else self.getOnlyTileNumbersRec(tiles[2:],tileNums+[tiles[1]]) 
    def areAllTilesSameNumber(self,tilesNum)->bool:
        return len(set(tilesNum))==1
    def areAllTilesSameNumberRec(self,tilesNum)->bool:
        return True if len(tilesNum)==0 else tilesNum[0]==tilesNum[-1] and self.areAllTilesSameNumberRec(tilesNum[1:-1])
    def isValidSequence(self,tilesNum):
        return all(tilesNum[i+1]-tilesNum[i]==1 for i in range(len(tilesNum)-1))
    def isValidSequenceRec(self,tilesNum:list)->bool:
        return True if len(tilesNum)<2 else tilesNum[0]==tilesNum[1]-1 and self.isValidSequenceRec(tilesNum[1:])
    def makeMove(self,tiles:list):
        if len(tiles)<3 or len(tiles)>14:return False,self.errorMessages[0]
        if not all(self.checkIfTileExists(tiles[i],tiles[i+1]) for i in range(0,len(tiles),2)):return False,self.errorMessages[1]
        if self.checkDuplicateTiles(tiles):return False,self.errorMessages[2]
        if sum(self.getOnlyTileNumbersRec(tiles,[]))<30 and self.hasPlayedFirstMove==False:return False,self.errorMessages[3]
        if not self.isValidSequence(self.getOnlyTileNumbersRec(tiles,[])) and self.hasPlayedFirstMove==False:return False,self.errorMessages[4]
        if not self.areAllTilesSameColorRec(tiles,set()) and not self.areAllTilesSameNumber(self.getOnlyTileNumbersRec(tiles,[])):return False,self.errorMessages[5]
        for i in range(0,len(tiles),2):self.placeTileOnTable(tiles[i],tiles[i+1])
        self.hasPlayedFirstMove=True
        return True,None
    def assignTile(self,tilesDeck):
        color=random.choice(list(self.tiles.keys()))
        number=random.choice([x for x in tilesDeck[color][0]+tilesDeck[color][1] if x!=0])
        self.addTileToPlayerTiles(color,number)
        tilesDeck[color][number not in tilesDeck[color][0]][number-1]=0
        return tilesDeck
    def sort(self,*args):
        {index.sort() for sub in self.tiles for index in self.tiles[sub]}