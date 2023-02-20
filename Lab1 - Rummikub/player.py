# DO NOT MODIFY EXISTING CODE - you may add helper classes if you deem necessary
import random

class Player:
    def __init__(self, name, tiles=None):
        self.name = name
        self.tiles = tiles if tiles is not None else {
            "red": [[], []],
            "blue": [[], []],
            "black": [[], []],
            "yellow": [[], []]
        }
        self.hasPlayedFirstMove = False
        self.errorMessages = [
            'Invalid Number of Tiles: Please select a valid number of tiles.',
            'Invalid Tiles: You passed in a tile or tiles that you do not currently have in your tiles set.',
            'Duplicate Tile: Duplicate tiles (tiles with the same number and color) in one tile set are not allowed.'
            'Invalid Move: Please make sure all your tiles add to at least 30.',
            'Invalid Sequence: please make sure that all numbers of the same color are in a sequence of +1 from each other, for example: 1,2,3 and not 1,2,4..',
            'Invalid Combination: please make sure that all numbers of different colors are the same number.'
        ]

    # DO NOT MODIFY
    def printTiles(self):
        print(self.name, "'s Tiles:")
        spaces = '    '
        for key in self.tiles:
            print('\t{}: {}{}'.format(key, spaces, self.tiles[key]))
            spaces = spaces[:-1]
        print()

    # TODO 1: Add a given tile to the player's tiles dictionary
    def addTileToPlayerTiles(self, color, number):
        self.tiles[color][(1 if number in self.tiles[color][0] else 0)].append(number)
        {x.sort() for x in self.tiles[color]}
        
        if number not in self.tiles[color][0]:
            self.tiles[color][0].append(number)
            self.tiles[color][0].sort()
        else:
            self.tiles[color][1].append(number)
            self.tiles[color][1].sort()

    # TODO 2: Randomly assign all 14 tiles for a game with 2-4 players

    def assignTiles(self, tilesDeck):
        while sum([len(x) for y in self.tiles.values() for x in y]) < 14:
            color = random.choice(list(self.tiles.keys()))
            number = random.choice([x for x in tilesDeck[color][0] if x != 0] + [x for x in tilesDeck[color][1] if x != 0])
            self.addTileToPlayerTiles(color, number)
            tilesDeck[color][0 if number in tilesDeck[color][0] else 1][tilesDeck[color][0 if number in tilesDeck[color][0] else 1].index(number)] = 0

    # EXTRA CREDIT 1
    def assignTilesRec(self, tilesDeck, numOfTiles): pass

    # TODO 3: Remove the given tile from the player's tiles dictionary
    def placeTileOnTable(self, color, number): 
        if number in self.tiles[color][0] or number in self.tiles[color][1]:
            self.tiles[color][1 if number in self.tiles[color][1] else 0].remove(number)
        else:
            print(self.errorMessages[1])

    # TODO 4: Check if the given tile does exist in the player's tiles dictionary
    def checkIfTileExists(self, color, number) -> bool: 
        return number in self.tiles[color][0] or number in self.tiles[color][1]

    # TODO 5: Check if the given list of tiles contains any duplicate tiles.
    # Duplicate tiles are tiles that are both the same number AND same color,
    # for example: 'red', 10 and 'red', 10 are duplicates, but 'blue', 10 and 'red', 10
    # would not be considered duplicates.
    def checkDuplicateTiles(self, tiles) -> bool:
        setlist = list(zip(tiles[0::2], tiles[1::2]))
        for i in setlist:
            if setlist.count(i) > 1: return True
        return False


    # TODO 6a: Check if the given list of tiles are all of the same color.
    def areAllTilesSameColor(self, tiles) -> bool:
        return len(set([x[0] for x in list(zip(tiles[0::2], tiles[1::2]))])) == 1

    # TODO 6b: Check, recursively, if the given list of tiles are all of the same color.
    # You must use a set.
    def areAllTilesSameColorRec(self, tiles, colorSet : set) -> bool:
        if len(tiles) == 0: return True
        else: return len(colorSet) == 1 and self.areAllTilesSameColorRec(tiles[1:], colorSet)

    # TODO 7: Given a list of tiles (color and number), return a list that contains only the tile numbers
    def getOnlyTileNumbersRec(self, tiles, tileNums : list) -> list:
        return [x[1] for x in tiles] if len(tiles) == 0 else self.getOnlyTileNumbersRec(tiles[1:], tileNums + [tiles[0][1]])

    # TODO 8a: Check if the given list of tile numbers (note, only numbers are passed in)
    # are all the same number
    def areAllTilesSameNumber(self, tilesNum) -> bool:
        return len(set(tilesNum)) == 1

    # TODO 8b: Check, recursively, if the given list of tile numbers (note, only numbers are passed in)
    # are all the same number
    def areAllTilesSameNumberRec(self, tilesNum) -> bool:
        if len(tilesNum) == 0: return True
        else: return len(set(tilesNum)) == 1 and self.areAllTilesSameNumberRec(tilesNum[1:])

    # TODO 9: Check if the given list of tile numbers (note, only numbers are passed in)
    # follow a valid sequence (desribed later)
    def isValidSequence(self, tilesNum) -> bool:
        return len(set(tilesNum)) == len(tilesNum) and max(tilesNum) - min(tilesNum) == len(tilesNum) - 1

    # EXTRA CREDIT 2
    def isValidSequenceRec(self, tilesNum: list) -> bool: pass

    # TODO 10: ALL PRIOR METHODS FROM #1 TO #9 MUST BE DONE BEFORE THIS ONE
    # Believe me, this will make your life easier
    # Feel free to write this method as you see fit, if you do not like the pseudocode and comments
    # I have written here. You are allowed to delete what is currently inside the method. However,
    # DO NOT modify the method signature. 
    def makeMove(self, tiles: list): pass
      # Need to check 5 things in order to validate the move
      # Be sure to return an error message for every instance where the check does not pass!

      # 1. Check that the player has chosen a minimum of 3 tiles and a maximum of 14 tiles
      # Here is some pseudocode to get you started:
      #if # player passed less than 3 tiles or more than 14:
        #return False, self.errorMessages[0]

      # 2. Check that the tiles the player passed in actually exist 
      # within the player's tiles dictionary (cool, we already have 
      # a method checks if ONE tile exists, we can use this somehow!)
      # TODO
      # Uncomment the following line and place it where appropriate
      # Look at what that error message says
      # return False, self.errorMessages[1] 

      # 3. Check that the player did not pass any duplicate tiles (hmm we have a method for this..)
      # you're on your own for this one, it's really just 2 lines of code

      # 4. Check that all the tiles add up to at minimum 30

      # 5. Check if all the colors of the tiles are the same (aww I gave you this one)
      #if self.areAllTilesSameColor(tiles):
        # 5a. If all the colors of the tiles are the same, check that they are a valid sequence
        # ...
        #if # it is not a valid sequence
          #return False, self.errorMessages[4]

        # If we get here, then it is a valid sequence!
        # First, place the tiles on the table

        # Then:
        #self.hasDrawnFirstMove = True
        # Last, we can return because this was a success! What do we return?
        #return # ....

      # 5b. If the color is not the same, we must check that all tiles are the same number
      #else:
        # I've given you a lot, this entire else is up to you!
        # Remember to return the correct error messages if some check does not pass

p = Player('Montse')
p.addTileToPlayerTiles('blue', 7)

assert p.tiles == {
    'red':     [[], []],
    'blue':    [[7], []],
    'black':   [[], []],
    'yellow':  [[], []]
}
tilesDeck = {
            "red": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "blue": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "black": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "yellow": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
        }
p.assignTiles(tilesDeck)
print(tilesDeck)
print(p.tiles)
p.placeTileOnTable('blue', 7)
print(p.tiles)

assert p.checkDuplicateTiles(['red', 10, 'red', 9, 'blue', 10]) == False
assert p.checkDuplicateTiles(['red', 10, 'red', 10, 'yellow', 8]) == True

assert p.areAllTilesSameColor(['red', 10, 'yellow', 9, 'blue', 10]) == False
assert p.areAllTilesSameColor(['red', 10, 'red', 1, 'red', 8, 'red', 9]) == True
assert p.areAllTilesSameColor(['black', 10, 'black', 9, 'blue', 10]) == False