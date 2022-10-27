import sys
from time import sleep

class Zwierz():
    __hunger = 0
    __mood = 1
    __name = ""
    __alive = True

    def __init__(self):
        if(self.__name == ""):
           newName = input("Nazwij mnie: ")
           self.setName(newName)


    def getName(self):
        return self.__name
    def getHunger(self):
        return self.__hunger
    def getMood(self):
        return self.__mood
    def getAlive(self):
        return self.__alive

    
    def setName(self, newName):
        self.__name = newName
    def setHunger(self, newHunger):
        self.__hunger = newHunger
    def setMood(self, newMood):
        self.__mood = newMood
    def setAlive(self, newAlive):
        self.__alive = newAlive


    def say(self, name, message):
        print(f"🐵 {name}: ", end="")
        for x in message:
            print(x, end="")
            sys.stdout.flush()
            sleep(0.1)
    
    def eat(self):
        if self.getHunger() >= 10:
            self.say(self.getName, "Nie jestem głodny")
        else:
            if self.getHunger() < 10:
                self.setHunger(10)
                self.say(self.getName, "Om nom nom nom")

        input()


