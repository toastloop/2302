from game import Rummikub
from player import Player

"""
## Part 1 - Player
In this part you will implement the Player class.
"""

"""
### #1) addTileToPlayerTiles()
1) Before the game begins, each player in the game has to be assigned 14 tiles at random. But before we implement this function, let us worry about adding just one tile to the player's tiles deck. 

Implement the **addTileToPlayerTiles()** function in the Player class which will, given a tile (color and number), add that tile to the Player's tiles. Your function must abide by the following constraint:
- Tiles should be added in ascending order regarding the arrays, as explained above
- Tiles should be sorted in ascending order within each array (i.e. [1,4,7] and not [4,1,7])

Hint: you do not need to check if a given tile already exists in **both** arrays, you need only check if it exists in the first array and from there you know where the tile belongs. This is because the tiles deck won't contain an extra tile (i.e., a third blue #7 tile), so you can assume that the tile given **will** be added to the Player's tiles.
"""
p = Player('Montse')
p.addTileToPlayerTiles('blue', 7)

assert p.tiles == {
    'red':     [[], []],
    'blue':    [[7], []],
    'black':   [[], []],
    'yellow':  [[], []]
}

# p.printTiles()
# should print:
# Montse 's Tiles:
#     red:     [[], []]
#     blue:    [[7], []]
#     black:   [[], []]
#     yellow:  [[], []]

p.addTileToPlayerTiles('blue', 7)
p.addTileToPlayerTiles('yellow', 10)
p.addTileToPlayerTiles('red', 3)
p.addTileToPlayerTiles('red', 1)

assert p.tiles == {
    'red':     [[1,3], []],
    'blue':    [[7], [7]],
    'black':   [[], []],
    'yellow':  [[10], []]
}

# p.printTiles()
# should print:
# Montse 's Tiles:
    # red:     [[1, 3], []]
    # blue:    [[7], [7]]
    # black:   [[], []]
    # yellow:  [[10], []]



"""
### #2) assignTiles()
2) Implement the **assignTiles()** method. This method will receive the tilesDeck from the Rummikub object. This method should do the following:
- Assign, at random, 14 tiles to the player (be sure to use the addTileToPlayerTiles() method you just created)
- Remove the assigned tiles from the tilesDeck (i.e. replace the corresponding number/color with a '0', as has been described earlier)

In order to accomplish this task, you will be using a Python module called 'random', specifically, there is one method that will be helpful for generating a random tile:
- **randint(a, b)**, where 'a' denotes the starting point and 'b' denotes the end point. This method returns a randomly generated integer between 'a' and 'b', inclusively (including both end points). 

Here is an example of how to use this method to generate a random number between 1 and 5, try running it multiple times!

Now that you understand how to use random, implement the **assignTiles()** method. Here are some hints:
- Use random to generate a random number and color for a tile (no, random does not generate random strings)
- Keep in mind that while you loop (**wow what a hint!**) and generate random tiles, you may generate a random tile that is no longer in the tilesDeck pile... oh what to do?

Test your implementation by running the code below and ensuring that each player gets 14 tiles assigned to them, and that none of the players get a third tile of the same number and color (for example, "Montse" has two red #3 tiles and "Daniel" has another red #3 tile...)
"""
game = Rummikub()
montse = Player("Montse")
daniel = Player("Daniel")
montse.assignTiles(game.tilesDeck)
daniel.assignTiles(game.tilesDeck)
assert sum([len(montse.tiles[color][0])+len(montse.tiles[color][1]) for color in montse.tiles])==14
assert sum([len(daniel.tiles[color][0])+len(daniel.tiles[color][1]) for color in daniel.tiles])==14

"""
### #3) placeTileOnTable()

Now that we can populate a player's tiles dictionary, we can start thinking about logistics of the game. One of the major moves of the game is for the player to be able to put down a chosen tile on the table. 

Implement the **placeTileOnTable()** method which will, given a tile (color and number), remove that tile from the player's tiles dictionary. 

**Note**: Do not worry about placing that removed tile on any specific table set, that part will come later. For now, think of this method as a "remove tile from player's tiles" method. 

Remember that if the given tile is a duplicate tile, it should be removed first from the second list. For example:

**DO NOT** worry about checking to see if the given tile exists within the player's tiles before removing it. You can assume that this method will never receive a nonexistent tile. This part will be handled by another method.


```
p.tiles = {
    'red':     [[1,3], []],
    'blue':    [[7], [7]], # let's say we want to remove a blue 7 tile
    'black':   [[], []],
    'yellow':  [[10], []]
}

# after calling:
p.placeTileOnTable('blue', 7)

# p.tiles should look like:
p.tiles = {
    'red':     [[1,3], []],
    'blue':    [[7], []], # note that it was the blue 7 in the second list that was removed, not the first one
    'black':   [[], []],
    'yellow':  [[10], []]
}
```

Test your implementation by running the following code:
"""
montse = Player("Montse")
daniel = Player("Daniel")
# feel free to create a third and/or fourth player to test as well

montse.addTileToPlayerTiles('red', 10)
montse.addTileToPlayerTiles('blue', 9)

daniel.addTileToPlayerTiles('yellow', 3)
daniel.addTileToPlayerTiles('yellow', 3)

montse.placeTileOnTable('red', 10)
assert montse.tiles == {
    'red':     [[], []],
    'blue':    [[9], []], 
    'black':   [[], []],
    'yellow':  [[], []]
}

daniel.placeTileOnTable('yellow', 3)
assert daniel.tiles == {
    'red':     [[], []],
    'blue':    [[], []], 
    'black':   [[], []],
    'yellow':  [[3], []]
}


"""
### #4) checkIfTileExists()

Now we can worry about checking if a given tile exists within the player's tiles dictionary. This method is self-explanatory:

Given a tile (color, number), check if it exists within the player's tiles dictionary. 
- If the tile does exist, return **True**
- If the tile does not exist, return **False**

Run the following code to test your implementation:
"""
montse = Player("Montse")
daniel = Player("Daniel")
# feel free to create a third and/or fourth player to test as well

montse.addTileToPlayerTiles('red', 10)
montse.addTileToPlayerTiles('blue', 9)

daniel.addTileToPlayerTiles('yellow', 3)
daniel.addTileToPlayerTiles('yellow', 3)

assert montse.checkIfTileExists('red', 10) == True
assert montse.checkIfTileExists('yellow', 1) == False

assert daniel.checkIfTileExists('yellow', 5) == False
assert daniel.checkIfTileExists('yellow', 3) == True


"""
### #5) checkDuplicateTiles()

When a player decides to place a set of tiles on the table, one of the important things we will need to check for is if the player has selected any duplicate tiles in their set.

Why? 

There are two kinds of moves a player can make with their tiles:
- tiles of the same color but different numbers
- tiles of the same number but different colors

(1) Tiles of the same color **must** be of different numbers (no duplicates) and must be in a valid numerical sequence (this will be explained in a later method)

(2) Tiles of the same number **must** be of different colors (no duplicates). This will also be explained in more detail in another method. 

For now, let us take things step by step and implement the **checkDuplicateTiles()** method which, given a list of tiles, checks if there are any duplicate tiles. 

A **duplicate** tile is a pair of tiles that are both the **same color and the same number**. For example, 'red' 10 and 'red' 10 would be duplicates, and they break both rules explained above. 

The method will be expecting a list in the following format: ['color', number, 'color', number...] This list is the list of tiles that the player has chosen to play (place on the table), and must therefore be checked before being played to make sure it is a valid move. This is one of many other methods we will implement to validate the player's move.

Here are some examples of lists that the method would expect:

```
['blue', 10, 'yellow', 4, 'black', 7] # denotes tiles: blue 10, yellow 4, and black 7

['red', 13, 'red', 1, 'red', 13] # denotes tiles red 13, red 1, and red 13
```

For this method, you **must assume** the following:
- A list will contain at least one tile (you will never receive an empty list)
- A list will always follow the format specified above
- A list will always be of an even length, never an odd length
- The color will always come before the number, and the color will always be a string
- The number will always come after the color, and the number will always be an integer
- Given that there is a method that already checks if a tile exists within a player's tiles dictionary (#4!), we do not need to check if the tiles in the passed list exist in the player's tiles dictionary

The method will:
- Return True if the list of tiles contains duplicate tiles
- Return False if the list of tiles does not contain any duplicate tiles

Run the following code to test your implementation:
"""
mayra = Player("Mayra")

assert mayra.checkDuplicateTiles(['red', 10, 'red', 9, 'blue', 10]) == False
assert mayra.checkDuplicateTiles(['red', 10, 'red', 10, 'yellow', 8]) == True


"""
### #6) areAllTilesSameColor() and areAllTilesSameColorRec()

**(a) areAllTilesSameColor()**

As explained briefly in #5, there are two main rules (there is a third one, but we'll discuss later) for when a player wants to place a set of tiles on the table: 

(1) Tiles of the same color **must** be of different numbers (no duplicates) and must be in a valid numerical sequence (this will be explained in a later method)

(2) Tiles of the same number **must** be of different colors (no duplicates). This will also be explained in more detail in another method. 

Implement the **areAllTilesSameColor()** method which will:
- Return True if all tiles in the list are of the same color
- Return False if at least one (or more) tiles in the list is a different color

Once again, the list that this method is expecting to receive is of the format ['color', number, 'color', number...] (see explanation from #5 for this list). 

For this method, you **must assume** the following (same assumptions as in #5):
- A list will contain at least one tile (you will never receive an empty list)
- A list will always follow the format specified above
- A list will always be of an even length, never an odd length
- The color will always come before the number, and the color will always be a string
- The number will always come after the color, and the number will always be an integer
- Given that there is a method that already checks if a tile exists within a player's tiles dictionary (#4!), we do not need to check if the tiles in the passed list exist in the player's tiles dictionary

**(b) areAllTilesSameColorRec()**

Implement the areAllTilesSameColorRec() method which will do the same exact thing as in (a), but must be implemented **recursively** and **must use a set**.

Run the following code to test your implementation:
"""
emilia = Player("Emilia")

assert emilia.areAllTilesSameColor(['red', 10, 'yellow', 9, 'blue', 10]) == False
assert emilia.areAllTilesSameColor(['red', 10, 'red', 1, 'red', 8, 'red', 9]) == True
assert emilia.areAllTilesSameColor(['black', 10, 'black', 9, 'blue', 10]) == False

s = set()

assert emilia.areAllTilesSameColorRec(['red', 1, 'red', 2, 'red', 3], s) == True
assert emilia.areAllTilesSameColorRec(['red', 1, 'red', 2, 'blue', 3], s) == False
assert emilia.areAllTilesSameColorRec(['yellow', 1, 'red', 2, 'blue', 3, 'blue', 8], s) == False

# add more test cases if needed

"""
### #7) getOnlyTileNumbersRec()

The next two methods you will write are a little different because they expect to receive a list of only numbers instead of a list of color and number. As such, implement the **getOnlyTilesNumbersRec()** method which will, given a list of tiles in the format ['color', number, 'color', number...] and given an empty list, returns a list which contains only the tile numbers.

For example, given:

```
# given input:
['red', 3, 'yellow', 9, 'black', 13], []
```
 The method should return:

```
[3,9,13]
```
But this is way too easy! Let's mix it up - this method **must** be implemented using **recursion**. You will only receive credit if you use recursion. 

Run the code below to test your implementation:
"""
montse = Player('Montse')

assert montse.getOnlyTileNumbersRec(['red', 10, 'yellow', 4, 'blue', 7], []) == [10,4,7]
assert montse.getOnlyTileNumbersRec(['blue', 3, 'yellow', 9, 'black', 1, 'red', 11], []) == [3,9,1,11]
assert montse.getOnlyTileNumbersRec(['yellow', 6, 'yellow', 4, 'blue', 10], []) == [6,4,10]

"""
### #8) areAllTilesSameNumber() and areAllTilesSameNumberRec()

**(a) areAllTilesSameNumber()**

Implement the **areAllTilesSameNumber()** method which, similar to the previous one (#6), checks if all the tile numbers passed in a list are the same. 

This method will:
- Return True if all of the numbers in the list are the same
- Return False if one or more of the numbers in the list are not the same

**Note**: This method takes in a tilesNum list, which **only contains integers** (nice! that makes it easier!).

**Note 2**: In order to receive full credit for this one, you **must** implement both the loop method and the recursive version of the method.

Here is an example of what a tilesNum list could look like:



```
[1,2,7,3,6,11]
```
Hint: Hmm, what is a great data structure that only allows me to insert one of each number.... something with an s? Of course, you can implement this in many ways, this is just one way:)

You **must** assume that the list that is passed will never be empty.

**(b) areAllTilesSameNumberRec()** 

Implement the **are areAllTilesSameNumberRec()** which does the exact same thing as in (a), but recursively. 

Run the following code to test your implementations:
"""
mayra = Player('Mayra')

assert mayra.areAllTilesSameNumber([10,10,10,11]) == False
assert mayra.areAllTilesSameNumber([3,3,3]) == True
assert mayra.areAllTilesSameNumber([7,1,7,9,7]) == False

assert mayra.areAllTilesSameNumberRec([1,1,1,1,1,1]) == True
assert mayra.areAllTilesSameNumberRec([2, 1, 1, 1, 1, 1]) == False
assert mayra.areAllTilesSameNumberRec([1, 1, 1, 1, 1, 2]) == False
# add more test cases if needed

"""
### 9) isValidSequence()

Remember that rule we were talking about earlier? The one about:

(1) Tiles of the same color **must** be of different numbers (no duplicates) and must be in a valid numerical sequence

Well now is the time to further discuss this rule. 

When a player chooses to play tiles of the same color, all the tiles must be different numbers, but they must also be in a numerical sequence (in ascending order) where the number to the right is only +1 greater than the one to the left. 

Confused? Here is an example of some sequences (assume all are red tiles):



```
[1,2,3,4,5] # valid sequence
[1,3,4,5,6] # invalid sequence, '3' is +2 of '1'

[8,9,10,11] # valid sequence
[5,6,10,11] # invalid sequence, '10' is +4 of '6'
```

The number directly to the right of a number must be +1 from the number directly to the left of it. 

Algorithmically:

nums[i] == nums[i+1] - 1
OR
nums[i+1] == nums[i] - 1

Implement the **isValidSequence() **method which will, given a tilesNum list that contains only integers, check if they are in a valid sequence. 

You must **assume** the following:
- You will never receive an empty list
- The list will only contain integers
- The list might NOT be sorted...and well, it's easier to check this if the list is sorted right? (hint hint)

The method will return:
- True if for every index i in the list of tilesNum, nums[i+1] **==** nums[i] - 1
- False if for at least one index i in the list of tilesNum, nums[i+1] **!=** nums[i] - 1

Run the following code to test your implementation:
"""
emilia = Player('Emilia')

assert emilia.isValidSequence([10,10,10,11]) == False
assert emilia.isValidSequence([1,2,3,4,5]) == True
assert emilia.isValidSequence([7,8,9,10,12]) == False

# add more test cases if needed

"""
### #10) makeMove()

**PLEASE READ BEFORE CONTINUING:**

This method is a combination of all prior methods (#1-#9) up to this point. In order to implement this method, you will use all of the methods from before. Be sure to have implemented all of them successfully before starting on this one, otherwise this method will be a lot more difficult. 

Ye be warned!

...

Welcome to the longest method you will write in this lab!

We just finished writing a bunch of smaller, easier methods. But why did we write so many small boolean checks?

In Rummikub, placing tiles is how the game is played, and the first move is perhaps the most complicated and special one. When the game begins and the players have been assigned their tiles, they cannot do anything until they have completed their first move of the game. 

The rules for a player's first move are as follows:
- All tiles must add to at least 30
- The player must select a minimum of 3 tiles up to a maximum of all of their tiles (their entire board, if they were that lucky and instantly win!)

A player cannot place any tiles on the table if they have not completed this special first move, no matter how many rounds into the game they are!

However, there is only one small difference between the first move and all other moves after that:
- After the first move, all tiles can add up to whatever number (so we don't have to check that they add up to at least 30 anymore!)

In the real game, after the first move, a player is allowed to place a minimum of 1 tiles on the table at a time. However, we will take care of this situation at another time. 

For the purposes of this method, the player must **always** choose at minimum three tiles to place on the table, so this must always be checked. 
Additionally, the player can choose a maximum of the total number of tiles they have, so this must also be checked. 

There are certain things that therefore must be checked within this method. 

In order to ensure that a player plays a valid move, implement the **makeMove()** method, which will validate all of the rules for making a play (notice that most of these validations have already been implemented in the other methods! Yay!).

This method takes in a list of tiles in the following format that we have seen in problems before:

['color', number, 'color', number...]

This method actually returns 2 things: a boolean and a string. 

The boolean denotes if the move was valid and they were therefore able to place their first tiles on the table. 

The string will be an error message. This error message will be returned when the boolean is False, and will describe the error in detail to the player. There are examples of how this works inside the method. For any questions, remember to go to office hours! We are here to help you.

Notice that the Player class contains a 'errorMessages' field, which is a list with different error messages. Some of these will be returned for you already (pre-coded), some will not. It will be up to you to determine which message is appropriate in which situation. 
**DO NO MODIFY OR DELETE ANY OF THE MESSAGES, DO NOT ADD ANY NEW MESSAGE.**

Remember, a message should only be returned when the boolean is False. When the boolean is True, then None will be returned in its place. Here is an example of what that would look like:



```
return True, None
```

**Note**: there is a field within Player called hasDrawnFirstMove. In this method, be sure to set this boolean to 'True' when the play has been found to be valid, and before the method returns True.

Here is a list of everything that this method needs to check for:
- If the player has not played their first move:
  - The player has selected a minimum of 3 tiles
  - All the tiles must add to at least 30
- If the player has already played their first move:
  - The tiles don't have to add up to anything

These rules apply to every move (from the first to the last one)
- The number of tiles a player has selected cannot exceed the total number of tiles they currently have
- The tiles the player wants to play actually exist within the player's tiles dictionary
- The player cannot play duplicate tiles
- If the color of all the tiles is the same, then: 
  - The tiles must be in a valid sequence (explained in #9)
- Else, if the color across all tiles is different, then:
  - The tiles must all be the same number

Remember to set the hasPlayedFirstMove field to true once the player has played their first move!

Run the code below to test your implementation:
"""
danielTiles = {
    "red": [[1, 3, 7, 10], [7]],
    "blue": [[1, 10], []],
    "black": [[10, 11, 12, 13], []],
    "yellow": [[1, 11, 13], []]
}
daniel = Player("Daniel", tiles=danielTiles)

# invalid number of tiles
isValid, errMsg = daniel.makeMove(['red', 10])
assert isValid == False
assert errMsg == daniel.errorMessages[0]

# tile that does not exist
isValid, errMsg = daniel.makeMove(['red', 7, 'blue', 4, 'yellow', 11])
assert isValid == False
assert errMsg == daniel.errorMessages[1]

# duplicate tiles
isValid, errMsg = daniel.makeMove(['red', 7, 'blue', 10, 'red', 7])
assert isValid == False
assert errMsg == daniel.errorMessages[2]

# add to 30
isValid, errMsg = daniel.makeMove(['red', 7, 'blue', 10, 'red', 1])
assert isValid == False
assert errMsg == daniel.errorMessages[3]

# same color, invalid sequence
isValid, errMsg = daniel.makeMove(['black', 10, 'black', 12, 'black', 13])
assert isValid == False
assert errMsg == daniel.errorMessages[4]

# same color, valid sequence, first move!
isValid, errMsg = daniel.makeMove(['black', 11, 'black', 12, 'black', 13])
assert isValid == True
assert errMsg == None

# different color, different numbers
isValid, errMsg = daniel.makeMove(['red', 1, 'blue', 10, 'black', 10])
assert isValid == False
assert errMsg == daniel.errorMessages[5]

# different color, same number, since already made first move, doesn't need to add to 30
isValid, errMsg = daniel.makeMove(['red', 1, 'blue', 1, 'yellow', 1])
assert isValid == True
assert errMsg == None

"""
## Part 2 - Rummikub

Now that we have a working Player class, we can focus on creating some of the game logic. 

We will focus mainly on setting up the game. The first thing we will do is create the players for the game, assign the tiles, then we can start giving each player options of what they want to do with their turn. 
"""

"""
### #1) setupPlayers()

First, implement the setupPlayers() method which will be the first method to run in the game. This method will welcome the players and then ask how many players are going to play (this part has already been done for you).

The method must:
- Validate that there are a minimum of 2 players and a maximum of 4 players
- For each player:
  - create a Player class by asking the name of each player
  - assign tiles
  - add the player to the list of players within the Rummikub class

Run the code below to test your implementation:
"""
# game = Rummikub()
# game.setupPlayers()

# assert (len(game.listOfPlayers) >= 2 and len(game.listOfPlayers) <= 4)
# for player in game.listOfPlayers:
#     assert player.name is not None
#     numOfTiles = 0
#     for color in player.tiles:
#         numOfTiles += len(player.tiles[color][0]) + len(player.tiles[color][1])
#     assert numOfTiles == 14

"""
### #2) parsePlayerInput()

Now that we have created our players, we are ready to start implementing some of the other logic of the game. 

When the player chooses to place tiles on the table, we will have to parse the input tiles that they give in order to create a list that our **makeMove()** method within the Player class can read. 

Remember, the **makeMove()** method takes in a list in the following format: ['color', number, 'color', number...]

The player will be expected to input a string in the following format: color number color number

Here are some examples of valid formats for player inputs for tiles:


```
red 10 blue 11 blue 12 black 1

blue 11 red 11 black 11
```

Implement the **parsePlayerInput()** method which will, given a string containing the tiles, returns a list (in the format mentioned above) and a string. The string will be an error message if an invalid format is given. Here is an example input and output:


```
# input:
black 1 black 2 black 3
# output:
['black', 1, 'black', 2, 'black', 3], None

# input:
black 1 2 3 red 10
# output:
None, errorMessages[0]
```

Remember that in this list, the color should be a string and the number should be an integer.

In addition, this method should return an error message from the errorMessages field within the Rummikub class to let the user know if they have inputted something in the invalid format.

Run the following code to test your implementation:
"""
game = Rummikub()

tilesList, errMsg = game.parsePlayerInput('yellow 1 yellow 2 yellow 3')
assert tilesList == ['yellow', 1, 'yellow', 2, 'yellow', 3]
assert errMsg == None

tilesList, errMsg = game.parsePlayerInput('yellow 1 2 3')
assert tilesList == None
assert errMsg == game.errorMessages[0]

"""
### #3) placeTilesOnTable()

Now that we can parse a player's input of tiles, we can implement the **placeTilesOnTable()** method which will, given a list of tiles in the parsed format (recall: ['color', number...]), will place these tiles on the table. That is, it will populate the tilesOnTable dictionary of the Rummikub class.

Do not worry about validating the tiles that are passed in (of these tiles being a valid player move), this will be done in another method. 

You **must** assume the following:
- This method will always receive a list of tiles in the valid format
- The list will never be empty (no need to check for empty list)
- No nonexistent, duplicate, other invalid tiles will be given

Simply add the tiles from tilesList to the tilesOnTable dictionary. 

Run the following code to test your implementation: 
"""

game = Rummikub()
game.placeTilesOnTable(['red', 1, 'red', 2, 'red', 3])
assert game.tilesOnTable['red'][0] == [1, 2, 3]

"""
### #4) takeTileFromTileDeck()

Implement the **takeTileFromTileDeck()** method which will generate, at random, a number and color for a tile that will be added to the player's tile deck if they choose to take a tile from the deck for their turn. 

This method should return the color and number of the tile that was added to the player's tile deck. This should be returned in the order color, number. 

Remember:
- Check that the randomly generated tile does indeed exist in the tile deck
- There already exists a method within the Player class to add a tile to the player's tile deck (#1 in Part 1!) 
- The tile should be removed from the tile deck once it is added to the player's tiles dictionary (remember how deleting tiles works, they are removed first from the second list then the first, and replaced with a '0', see the description of the Rummikub Class under the Introduction section above for more information).

Run the code below to test your implementation:
"""
danielTiles = {
    "red": [[1, 3, 7, 10], [7]],
    "blue": [[1, 10], []],
    "black": [[10, 11, 12, 13], []],
    "yellow": [[1, 11, 13], []]
}

daniel = Player("Daniel", tiles=danielTiles)
game = Rummikub()
game.currentPlayer = daniel

numOfTilesBefore = 0
for c in daniel.tiles:
    numOfTilesBefore += len(daniel.tiles[c][0]) + len(daniel.tiles[c][1])

color, num = game.takeTileFromTileDeck()

numOfTilesAfter = 0
for c in daniel.tiles:
    numOfTilesAfter += len(daniel.tiles[c][0]) + len(daniel.tiles[c][1])


assert numOfTilesBefore == (numOfTilesAfter - 1)
assert (num in daniel.tiles[color][0] or num in daniel.tiles[color][1])
assert (game.tilesDeck[color][0][num-1] == 0  or game.tilesDeck[color][1][num-1] == 0)

"""
### #5) play()

Finally we have reached the last method for this lab! Given that Rummikub can be a very long game, we will not be coding it in it's entirety.

Implement the **play()** method which will start the game. This method **must** meet the following requirements:
- Since we are not going to code the entire game, we will only be playing five rounds of the game. The **play()** method will allow all players to play 5 rounds of the game.
- Each round should print all tiles that are currently on the table (there is a helper method already written that does this)
- One round = every player taking a turn, therefore 5 rounds = every player played 5 turns. 1 round = 1 turn per player
- For every player's turn:
  - Print the name of the player whose turn it is
  - Print the tiles for that player
  - Print the turn options (this is also a pre-made helper method)
  - Validate that the player has chosen a valid move for their turn (notice how there are 3 things a player can choose to do in their turn, validate they choose something valid) and print an error message if they choose something invalid. Their turn is not over until they choose a valid move (don't skip the player if they choose an invalid move, allow them to choose again)
  - Implement the corresponding action for each option (take a look at the **printTurnOptions()** method for this)
  - If the player chooses option #1:
    - Remember to validate the player's move, and to print the error message if the move was invalid, and allow them to try again until the move is valid
    - Remember to update the tiles on the table
    - If the player realizes that there is no valid move for them to make, this will make them stay stuck in an infinite loop because validMove would be false. Therefore, allow the player to input 'nevermind', which would take them back to choose a different play option
  - If the player chooses option #2:
    - Print the random tile that the player took from the deck so that they know which one it was
    - Print their current tiles again so they can see their updated tiles 
  - If the player chooses option #3: 
    - The game is over and the program should stop running (no other players will take a turn)
  - If the player chooses an invalid option, bring the corresponding error message (see the errorMessages field within the Rummikub class)

You will have to be creative when testing your implementations to be sure that every player can make a move, every player has their tiles, the tiles are updated correctly, etc., and that your code will not fail. Testing for this one will be left up to you.
"""
game = Rummikub()
game.setupPlayers()
game.play()

"""
Notice that within the Player class, there are two methods that have a comment of "EXTRA CREDIT". 

For extra credit, implement these methods recursively. 

In order to receive full credit: 
- You must use recursion. You will receive 0 points if you do not use recursion.
- You must write test cases to test your implementations. Be sure your test cases are thorough and cover all possible cases (note: you are allowed to make the same assumptions for these methods as for the original version of these methods, take a look at those if you don't remember)

Don't worry about testing these methods for the entire Rummikub play() instance. These just have to run on their own.

Be sure to test your implementation! You will not receive full credit if you do not write test cases. 
"""

"""
### #1) assignTilesRec()

Worth: 5 extra points

See Part 1 - Player, #2, for the description of this method. Implement it recursively. Remember to write your test cases.
"""

game = Rummikub()

montse = Player("Montse")
daniel = Player("Daniel")

montse.assignTilesRec(game.tilesDeck, 14)
daniel.assignTilesRec(game.tilesDeck, 14)

numOfTiles = 0
for color in montse.tiles:
    numOfTiles += len(montse.tiles[color][0]) + len(montse.tiles[color][1])
assert numOfTiles == 14

numOfTiles = 0
for color in daniel.tiles:
    numOfTiles += len(daniel.tiles[color][0]) + len(daniel.tiles[color][1])
assert numOfTiles == 14

"""
### #2) isValidSequenceRec()

Worth: 3 extra points

See Part 1 - Player, #9, for the description of this method. Implement it recursively. Remember to write your test cases.
"""

emilia = Player('Emilia')

assert emilia.isValidSequenceRec([10,10,10,11]) == False
assert emilia.isValidSequenceRec([1,2,3,4,5]) == True
assert emilia.isValidSequenceRec([7,8,9,10,12]) == False