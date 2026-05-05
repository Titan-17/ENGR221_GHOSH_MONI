"""
Author: Prof. Alyssa
The Controller of the game, including handling key presses
and AI mode.

Adapted from HMC CS60

Hi, My name is Moni Ghosh, and this file was updated on 5th May.
"""

from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue


class Controller:
    def __init__(self):
        self.__data = GameData()
        self.__display = BoardDisplay()
        self.__numCycles = 0
        self.__cameFrom = {}

        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None

        self.startNewGame()

    def startNewGame(self):
        """ Initializes the board for a new game """
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """
        clock = pygame.time.Clock()

        while not self.__data.getGameOver():
            self.cycle()
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self):
        """ The main behavior of each time step """
        self.checkKeypress()
        self.updateSnake()
        self.updateFood()
        self.__numCycles += 1
        self.__display.updateGraphics(self.__data)

    def checkKeypress(self):
        """ Update the game based on user input """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOver()

            elif event.type == pygame.KEYDOWN:
                if event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()

                elif event.key in self.Keypress.AI.value:
                    self.__data.setAIMode()

                elif event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()

                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()

                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()

                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()

    def updateSnake(self):
        """ Move the snake forward one step """
        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            if self.__data.inAIMode():
                nextCell = self.getNextCellFromBFS()
            else:
                nextCell = self.__data.getNextCellInDir()

            try:
                self.advanceSnake(nextCell)
            except:
                print("Failed to advance snake")

    def advanceSnake(self, nextCell):
        """ Move the snake's head to the given cell """
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()

        elif nextCell.isFood():
            self.playSound_eat()
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
        """ Use BFS to find the closest food and return the next cell on that path """
        self.__data.resetCellsForSearch()

        cellsToSearch = Queue()
        self.__cameFrom = {}

        head = self.__data.getSnakeHead()
        head.setAddedToSearchList()
        cellsToSearch.put(head)
        self.__cameFrom[head] = None

        foodCell = None

        while not cellsToSearch.empty():
            current = cellsToSearch.get()

            if current.isFood():
                foodCell = current
                break

            for neighbor in self.__data.getNeighbors(current):
                if neighbor in self.__cameFrom:
                    continue

                if neighbor.isWall() or neighbor.isBody():
                    continue

                self.__cameFrom[neighbor] = current
                neighbor.setAddedToSearchList()
                cellsToSearch.put(neighbor)

        if foodCell is not None:
            return self.getFirstCellInPath(foodCell)

        return self.__data.getRandomNeighbor(head)

    def getFirstCellInPath(self, foodCell):
        """ Return the first cell from the snake head toward the food cell """
        head = self.__data.getSnakeHead()

        if foodCell == head:
            return head

        current = foodCell

        while (
            current in self.__cameFrom
            and self.__cameFrom[current] is not None
            and self.__cameFrom[current] != head
        ):
            current = self.__cameFrom[current]

        if current not in self.__cameFrom:
            return self.__data.getRandomNeighbor(head)

        return current

    def reverseSnake(self):
        """ Reverse the snake """
        self.__data.reverseSnake()

    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ Valid keyboard inputs """
        UP = pygame.K_i, pygame.K_UP
        DOWN = pygame.K_k, pygame.K_DOWN
        LEFT = pygame.K_j, pygame.K_LEFT
        RIGHT = pygame.K_l, pygame.K_RIGHT
        REVERSE = pygame.K_r,
        AI = pygame.K_a,


if __name__ == "__main__":
    Controller().run()