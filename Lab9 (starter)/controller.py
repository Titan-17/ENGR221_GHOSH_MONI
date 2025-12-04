"""
Author: Prof. Alyssa
The Controller of the game, including handling key presses
(and AI in the next assignment). You will update this file.

Adapted from HMC CS60

Hi, My name is Moni Ghosh, and this File was updated on 12th Nov
"""
from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue

class Controller():
    def __init__(self):
        # The current state of the board
        self.__data = GameData()
        # The display
        self.__display = BoardDisplay()
        # How many frames have passed
        self.__numCycles = 0
        # Used by BFS to reconstruct paths from the head to a food cell
        self.__cameFrom = {}

        # Attempt to load any sounds and images
        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None

        # Initialize the board for a new game
        self.startNewGame()
        
    def startNewGame(self):
        """ Initializes the board for a new game """

        # Place the snake on the board
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """

        # Keep track of the time that's passed in the game 
        clock = pygame.time.Clock()

        # Loop until the game ends
        while not self.__data.getGameOver():
            # Run the main behavior
            self.cycle() 
            # Sleep
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self):
        """ The main behavior of each time step """

        # Check for user input
        self.checkKeypress()
        # Update the snake state
        self.updateSnake()
        # Update the food state
        self.updateFood()
        # Increment the number of cycles
        self.__numCycles += 1
        # Update the display based on the new state
        self.__display.updateGraphics(self.__data)

    def checkKeypress(self):
        """ Update the game based on user input """
        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.gameOver()
            # Change the snake's direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                # Reverse direction of snake
                if event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()
                # Enter AI mode
                elif event.key in self.Keypress.AI.value:
                    self.__data.setAIMode()
                # Change directions
                    
                elif event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()
                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()
                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()
                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()


    def updateSnake(self):
        """ Move the snake forward one step, either in the current 
            direction, or as directed by the AI """

        # Move the snake once every REFRESH_RATE cycles
        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            # Find the next place the snake should move
            if self.__data.inAIMode():
                nextCell = self.getNextCellFromBFS()
            else:
                nextCell = self.__data.getNextCellInDir()
            try:
                # Move the snake to the next cell
                self.advanceSnake(nextCell)
            except:
                print("Failed to advance snake")

    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """

        # If we run into a wall or the snake, it's game over
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()
        
        # If we eat food, update the state of the board
        elif nextCell.isFood():
            self.playSound_eat()
            # TODO Tell __data that we ate food!

            self.__data._eatAt(nextCell)     
            self.__data._makeNewHead(nextCell)

        else:
            self.__data._makeNewHead(nextCell)
            self.__data._removeTail()


    def updateFood(self):
        """ Add food every FOOD_ADD_RATE cycles or if there is no food """
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """ Uses BFS to search for the food closest to the head of the snake.
            Returns the *next* step the snake should take along the shortest path
            to the closest food cell. """
        
        # Prepare all the tiles to search
        self.__data.resetCellsForSearch()

        # Initialize a queue to hold the tiles to search
        cellsToSearch = Queue()

        # Clear any previous BFS state
        self.__cameFrom = {}

        # Add the head to the queue and mark it as added
        head = self.__data.getSnakeHead()
        head.setAddedToSearchList()
        cellsToSearch.put(head)
        self.__cameFrom[head] = None

        foodCell = None

        # Standard BFS
        while not cellsToSearch.empty():
            current = cellsToSearch.get()

            # If we found food, stop searching
            if current.isFood():
                foodCell = current
                break

            # Explore valid neighbors of the current cell
            for neighbor in self.__data.getNeighbors(current):
                # Skip walls, snake body, and already-visited cells
                if neighbor in self.__cameFrom:
                    continue
                if neighbor.isWall() or neighbor.isBody():
                    continue

                # Record how we reached this neighbor and add to queue
                self.__cameFrom[neighbor] = current
                neighbor.setAddedToSearchList()
                cellsToSearch.put(neighbor)

        # If we found a food cell, return the first step along the path to it
        if foodCell is not None:
            return self.getFirstCellInPath(foodCell)

        # If the search failed, return a random neighbor
        return self.__data.getRandomNeighbor(head)

    def getFirstCellInPath(self, foodCell):
        """ Given the food cell found by BFS, walk backwards using the
            parent relationships recorded in self.__cameFrom until we
            reach the cell that is one step away from the head. That cell
            is the next move the snake should take. """

        head = self.__data.getSnakeHead()

        # If for some reason the food *is* the head, just stay put
        if foodCell == head:
            return head

        current = foodCell

        # Walk backwards until the parent of 'current' is the head.
        # Then 'current' is the first step on the path from head to food.
        while current in self.__cameFrom and self.__cameFrom[current] is not None \
                and self.__cameFrom[current] != head:
            current = self.__cameFrom[current]

        # If we somehow didn't record a path, fall back to a random neighbor
        if current not in self.__cameFrom:
            return self.__data.getRandomNeighbor(head)

        return current
    
    def reverseSnake(self):
        """ Reverse the direction that the snake is moving, effectively
            swapping the head and tail and flipping the motion direction.

            The low-level details of reversing the internal snake cells
            and its direction are handled by GameData.
        """
        self.__data.reverseSnake()

    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ An enumeration (enum) defining the valid keyboard inputs 
            to ensure that we do not accidentally assign an invalid value.
        """
        UP = pygame.K_i, pygame.K_UP        # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN    # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT    # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT  # l and right arrow key
        REVERSE = pygame.K_r,               # r
        AI = pygame.K_a,                    # a


if __name__ == "__main__":
    Controller().run()
