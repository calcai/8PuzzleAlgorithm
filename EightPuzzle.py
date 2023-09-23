import random
from queue import PriorityQueue, Empty

class EightPuzzle():

    #constructor
    def __init__(self):
        self.puzzle = [[],[],[]]
        self.zero = []
        self.pastmoves = []
        self.nummoves = 0

    # creates the state based on sequence input and places in 2D array with 3 rows and 3 columns
    # also sets the zero from inital state
    # input sequence in string form "012 345 678", where spaces indicate new row
    def setState(self, sequence):
        self.puzzle = [[],[],[]]
        r = sequence.split()
        for n,i in enumerate(r):
            for j in range(3):
                self.puzzle[n].append(int(i[j]))
                if i[j] == "0":
                    self.zero = [j, n]

    def printState(self):
        state = ""
        for r in self.puzzle:
            for i in r:
                state += str(i)
            state += " "
        print(state)

    #helper method
    def getState(self):
        state = ""
        for r in self.puzzle:
            for i in r:
                state += str(i)
            state += " "
        return state
        
    # easier print to read board
    def printBoard(self):
        for r in self.puzzle:
            print(r)
    
    def move(self, dir) -> bool:
        '''move_methods = {
            "up": self.up(),
            "down": self.down(),
            "left": self.left(),
            "right": self.right()
        }
        if dir in move_methods:
            return move_methods[dir]'''
        if dir == "up":
            return self.up()
        if dir == "down":
            return self.down()
        if dir == "left":
            return self.left()
        if dir == "right":
            return self.right()

    # helper methods for move method that do the swap
    # simultaneously swap the locations and set the new zero location
    def up(self):
        if self.zero[1] == 0:
            return False
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1] - 1][self.zero[0]] = self.puzzle[self.zero[1] - 1][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[1] -= 1
        return True
    def down(self):
        if self.zero[1] == 2:
            return False
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1] + 1][self.zero[0]] = self.puzzle[self.zero[1] + 1][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[1] += 1
        return True
    def left(self):
        if self.zero[0] == 0:
            return False
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0] - 1] = self.puzzle[self.zero[1]][self.zero[0] - 1], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[0] -= 1
        return True
    def right(self):
        if self.zero[0] == 2:
            return False
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0] + 1] = self.puzzle[self.zero[1]][self.zero[0] + 1], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[0] += 1
        return True

    def randomizeState(self, n):
        self.setState("012 345 678")
        while n > 0:
            randnum = random.randint(0,3)
            if randnum == 0:
                if self.move("up"):
                    n -= 1
            elif randnum == 1:
                if self.move("down"):
                    n -= 1
            elif randnum == 2:
                if self.move("left"):
                    n -= 1
            elif randnum == 3:
                if self.move("right"):
                    n -= 1

    def solveAStar(self, heuristic):
        pq = PriorityQueue()
        if heuristic == "h1":
            while not self.solved():
                self.nummoves += 1
                up, down, left, right = self.h1up(), self.h1down(), self.h1left(), self.h1right()
                if self.move("up"):
                    pq.put((self.nummoves + up, self.getState(), self.pastmoves + ["up"], self.nummoves))
                    self.move("down")
                if self.move("down"):
                    pq.put((self.nummoves + down, self.getState(), self.pastmoves + ["down"], self.nummoves))
                    self.move("up")
                if self.move("left"):
                    pq.put((self.nummoves + left, self.getState(), self.pastmoves + ["left"], self.nummoves))
                    self.move("right")
                if self.move("right"):
                    pq.put((self.nummoves + right, self.getState(), self.pastmoves + ["right"], self.nummoves))
                    self.move("left")
                func, state, moves, n = pq.get()
                self.setState(state)
                self.pastmoves = moves
                self.nummoves = n
            for i in self.pastmoves:
                print(i)
                    
        elif heuristic == "h2":
            return
        
    #helper method to check if solved
    def solved(self) -> bool:
        if self.puzzle != [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            return False
        return True

    #helper methods to find heuristic 1
    def h1up(self):
        if self.move("up"):
            h = 0
            for n, i in enumerate(self.puzzle):
                for m, j in enumerate(i):
                    if j != n * 3 + m:
                        h += 1
            self.move("down")
            return h
        else:
            return float('inf')
    def h1down(self):
        if self.move("down"):
            h = 0
            for n, i in enumerate(self.puzzle):
                for m, j in enumerate(i):
                    if j != n * 3 + m:
                        h += 1
            self.move("up")
            return h
        else:
            return float('inf')
    def h1left(self):
        if self.move("left"):
            h = 0
            for n, i in enumerate(self.puzzle):
                for m, j in enumerate(i):
                    if j != n * 3 + m:
                        h += 1
            self.move("right")
            return h
        else:
            return float('inf')
    def h1right(self):
        if self.move("right"):
            h = 0
            for n, i in enumerate(self.puzzle):
                for m, j in enumerate(i):
                    if j != n * 3 + m:
                        h += 1
            self.move("left")
            return h
        else:
            return float('inf')


def main():
    test = EightPuzzle()
    test.randomizeState(50)
    test.printBoard()
    print(test.h1up())
    print(test.h1down())
    print(test.h1left())
    print(test.h1right())
    test.solveAStar("h1")
    test.printBoard()
if __name__=="__main__":
    main()