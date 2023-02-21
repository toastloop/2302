from player import Player
import random
class Rummikub:
    def __init__(self):
        self.tilesDeck = {"red": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "blue": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "black": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "yellow": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]}
        self.tilesOnTable = {"red": [[], []],"blue": [[], []],"black": [[], []],"yellow": [[], []]}
        self.errorMessages = ['Invalid format: please make sure you input your tiles in the following format (color number) for example:\nblue 10 red 11']
        self.listOfPlayers: list[Player] = []
        self.currentPlayer: Player
        self.validMove = False
        self.gameOver = False
    def printTilesTable(self):
        print('Current Table:');
        [print('\t{}:\t{}'.format(key, self.tilesDeck[key])) for key in self.tilesDeck]
    def printTurnOptions(self):
        print('1. Place tile(s) on table\n2. Take a tile from the deck of tiles (ends your turn)\n3. View my tiles')
    def setupPlayers(self):
        print("Welcome to Rummikub!")
        for i in range(int(input('Input the number of players: '))):
            self.listOfPlayers.append(Player(input('Input the name of player {}: '.format(i+1))))
            self.listOfPlayers[i].assignTiles(self.tilesDeck)
    def parsePlayerInput(self, tilesStr):
        output=[int(str) if str.isnumeric() else str.lower() for str in tilesStr.split()]
        error=all([type(output[i])!=type(output[i-1]) for i in range(len(output)-1)])
        return output if error else None, None if error else self.errorMessages[0]
    def placeTilesOnTable(self, tilesList):
        {
            self.tilesOnTable[tilesList[i]][1 if tilesList[i+1] in self.tilesOnTable[tilesList[i]][0] else 0].append(tilesList[i+1]) for i in range(0, len(tilesList), 2)
        }
    def takeTileFromTileDeck(self):
        color=str(random.choice(list(self.tilesDeck.keys())))
        num=random.choice([x for x in self.tilesDeck[color][0]+self.tilesDeck[color][1] if x!=0])
        self.currentPlayer.addTileToPlayerTiles(color,num)
        self.tilesDeck[color][1 if num in self.tilesDeck[color][1] else 0][num - 1] = 0
        return color,num
    def play(self):
        print('We are ready to start the game!')
        for i in range(len(self.listOfPlayers)*5):
            self.currentPlayer=self.listOfPlayers[i%len(self.listOfPlayers)]
            print(f"{self.currentPlayer.name}'s Turn")
            self.currentPlayer.printTiles()
            while self.validMove==False:
                self.printTurnOptions()
                match int(input("Choose an option: ")):
                    case 1:
                        while self.validMove==False:
                            tiles=input("Input your tiles: ")
                            if tiles.lower()=="nevermind":break
                            tiles,error=self.parsePlayerInput(tiles)
                            if tiles==None:print(error);continue
                            success,error=self.currentPlayer.makeMove(tiles)
                            if success==False:print(error);continue
                            self.placeTilesOnTable(tiles)
                            self.printTilesTable()
                            self.validMove=True
                    case 2:
                            color,num=self.takeTileFromTileDeck()
                            print(f"You took a tile from the deck: {color} {num}")
                            self.currentPlayer.printTiles()
                            self.validMove=True
                    case 3:
                            self.gameOver=True
                            self.validMove=True
                    case _: print("Invalid choice!")
            if(self.gameOver):break
            self.validMove=False
        print("Game Over!")