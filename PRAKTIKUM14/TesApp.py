import MyLib as l
import math

def main():
    level = input("EASY, MEDIUM atau HARD : ")
    optLevel = ["EASY", "MEDIUM", "HARD"]
    if level.upper() not in optLevel :
        print("Maaf pilihan kamu salah")
        return

    l.initScreen(0, 10, 0, 10)
    l.setPlayerPosition(0, 0)
    l.setGoal()
    l.spawnEnemies(level)
    l.displayInitStats(level)

    while True :
        move = input("UP, DOWN, LEFT, atau RIGHT : ")
        optMove = ["UP", "DOWN", "LEFT", "RIGHT"]
        if move.upper()  not in optMove :
            print("Maaf pilihan kamu salah")
            break
        if l.checkPlayerMove(move) == False :
            break

if __name__ == "__main__":
    main()