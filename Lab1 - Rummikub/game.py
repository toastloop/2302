# DO NOT MODIFY EXISTING CODE - you may add helper classes if you deem necessary
class Rummikub:
  
      def __init__(self):
        self.tilesDeck = {
            "red": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "blue": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "black": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
            "yellow": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
        }
        self.tilesOnTable = {
            "red": [[], []],
            "blue": [[], []],
            "black": [[], []],
            "yellow": [[], []]
        }
        self.errorMessages = [
            'Invalid format: please make sure you input your tiles in the following format (color number) for example:\nblue 10 red 11',
        ]
        self.listOfPlayers: list[Player] = []
        self.currentPlayer: Player
        self.validMove = False
        self.gameOver = False

        def printTilesTable(self):
            print('Current Table:')
            spaces = '    '
            for key in self.tilesDeck:
                print('\t{}: {}{}'.format(key, spaces, self.tilesDeck[key]))
                spaces = spaces[:-1]
            print()

        def printTurnOptions(self):
            print('1. Place tile(s) on table\n')
            print('2. Take a tile from the deck of tiles (ends your turn)')
            print('3. View my tiles')

        # TODO 1
        def setupPlayers(self):
            print("Welcome to Rummikub!")
            numPlayers = int(input('Input the number of players: '))
            # Your turn

        # TODO 2
        def parsePlayerInput(self, tilesStr):
          pass

        # TODO 3
        def placeTilesOnTable(self, tilesList):
          pass

        # TODO 4
        def takeTileFromTileDeck(self):
          pass

        # TODO 5
        def play(self):
            print('We are ready to start the game!')
            # you will have to use the following somewhere in this method:
            # self.printTilesTable()
            # self.currentPlayer = ...
            # self.validMove = ...
            # self.printTurnOptions()
            # self.gameOver = ...