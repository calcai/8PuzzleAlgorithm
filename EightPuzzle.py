import random

class EightPuzzle():

    #constructor
    def __init__(self):
        self.puzzle = [[],[],[]]
        self.zero = []

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
    
    # easier print to read board
    def printBoard(self):
        for r in self.puzzle:
            print(r)
    
    def move(self, dir):
        if not (dir == "up" or dir == "down" or dir == "left" or dir == "right"):
            return False
        if dir == "up":
            if self.zero[1] == 0:
                return False
            else:
                self.up()
        if dir == "down":
            if self.zero[1] == 2:
                return False
            else:
                self.down()
        if dir == "left":
            if self.zero[0] == 0:
                return False
            else:
                self.left()
        if dir == "right":
            if self.zero[0] == 2:
                return False
            else:
                self.right()
        return True

    # helper methods for move method that do the swap
    # simultaneously swap the locations and set the new zero location
    def up(self):
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1] - 1][self.zero[0]] = self.puzzle[self.zero[1] - 1][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[1] -= 1
    def down(self):
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1] + 1][self.zero[0]] = self.puzzle[self.zero[1] + 1][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[1] += 1
    def left(self):
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0] - 1] = self.puzzle[self.zero[1]][self.zero[0] - 1], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[0] -= 1
    def right(self):
        self.puzzle[self.zero[1]][self.zero[0]], self.puzzle[self.zero[1]][self.zero[0] + 1] = self.puzzle[self.zero[1]][self.zero[0] + 1], self.puzzle[self.zero[1]][self.zero[0]]
        self.zero[0] += 1

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
        if heuristic == "h1":
            up, down, left, right = self.h1up, self.h1down, self.h1left, self.h1right
        elif heuristic == "h2":
            return
        
    def solved(self) -> bool:
        key = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for i in range(3):
            for j in range(3):
                if self.puzzle[i, j] != key[i,j]:
                    return False
        return True

    
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
    test.setState("012 345 678")
    test.printBoard()
    if test.solved:
        print(0)
    test.randomizeState(1000)
    test.printBoard()
    if test.solved:
        print(0)
    
if __name__=="__main__":
    main()