from secrets import choice
import sys
import os
import time
import random

class Zwierz():
    __hunger = 0
    __mood = 1
    __name = ""
    __aliveStatus = True

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
    def getStatus(self):
        return self.__aliveStatus
    def getHungerText(self):
        num = self.getHunger()
        if num == 0:
            return "Głodny..."
        elif num == 10:
            return "Najedzony :D"
        else: 
            return "Nie wiem"

    def getMoodText(self):
        num = self.getMood()
        if num == 1:
            return "Wściekły"
        elif num == 2:
            return "Poddenerwowany"
        elif num == 3:
            return "Zadowolony"
        elif num == 4:
            return "Szczęśliwy"
        else:
            return "Dziwny"

    
    def setName(self, newName):
        self.__name = newName
    def setHunger(self, newHunger):
        self.__hunger = newHunger
    def setMood(self, newMood):
        self.__mood = newMood
    def setStatus(self, newStatus):
        self.__aliveStatus = newStatus


    def say(self, name, message):
        print(f"🐵 {name}: ", end="")
        for x in message:
            print(x, end="")
            sys.stdout.flush()
            time.sleep(0.1)
    
    def eat(self):
        os.system("cls")
        if self.getHunger() >= 10:
            self.say(self.getName(), "Nie jestem głodny")
        else:
            if self.getHunger() < 10:
                self.setHunger(10)
                self.say(self.getName(), "Om nom nom nom")
                if self.getMood() != 4:
                    self.setMood(self.getMood() + 1)
                

        input("\nKoniec karmienia? - Enter")

    def ballAnim(self):
        os.system("cls")
        print("🐵⚽......🥅")
        time.sleep(1)
        os.system("cls")
        print("🐵..⚽....🥅")
        time.sleep(1)
        os.system("cls")
        print("🐵....⚽..🥅")
        time.sleep(1)
        os.system("cls")
        print("🐵......⚽🥅")
        time.sleep(1)
        os.system("cls")
        print("💖🐵💖")

    def UgotowanieAnim(self):
        os.system("cls")
        t = 60
        for i in range(0, 60):
            print(f"🍲 Gotowanie: {t}s")
            time.sleep(1)
            t -= 1
            os.system("cls")
        input("\nEnter - Dalej")

    def play(self):
        os.system("cls")
        self.ballAnim()
        if self.getMood() <= 2:
            self.setMood(self.getMood() + 2)
        else:
            self.setMood(4)
        
        input("Koniec zabawy? - Enter")

    def dialogue(self):
        os.system("cls")
        options = [
            "Schowaj się!",
            "Boooo!",
            "Pobawmy się!",
            "Nie można polizać łokcia.",
            "Serce krewetki jest w głowie.",
            "Krokodyl nie potrafi wystawić języka.",
            "Świnie nie mogą fizycznie spojrzeć w niebo.",
            "Jeśli kichasz zbyt mocno, możesz złamać żebro."
        ]
        if self.getMood() == 1:
            self.say(self.getName(), "Nie rozmawiam z tobą.")
            input("\nEnter - Dalej")
        else:
            self.say(self.getName(), random.choice(options))
            if self.getMood() < 4:
                self.setMood(self.getMood() + 1)
            input("\nEnter - Dalej")
    
    def information(self):
        os.system("cls")
        self.say(self.getName(), f"Mam na imię: {self.getName()}")
        input("\nEnter - Dalej")
        os.system("cls")
        self.say(self.getName(), f"Poziom głodu: {self.getHungerText()}")
        input("\nEnter - Dalej")
        os.system("cls")
        self.say(self.getName(), f"Nastrój: {self.getMoodText()}")
        input("\nEnter - Dalej")
        os.system("cls")
    
    def dyingMethods(self):
        os.system("cls")
        print("""
            =================================
            | 0 - Ugotowanie                |
            | 1 - Trucizna                  |
            | 2 - Praca klasowa             |
            | 3 - Spopielenie               |
            | 4 - Siekiera                  |
            =================================
        """)
        method = input("Wybierz śmierć?: ")
        if method == "0":
            self.UgotowanieAnim()

    def die(self):
        os.system("cls")
        if self.getStatus() == True:
            self.dyingMethods()
        else:
            self.say(self.getName, "Ja już nie żyje...")


class Program():
    pet = Zwierz()
    
    def choice(self, action):
        if action == "0":
            Program.pet.information()
        elif action == "1":
            Program.pet.eat()
        elif action == "2":
            Program.pet.play()
        elif action == "3":
            Program.pet.dialogue()
        elif action == "4":
            Program.pet.die()
        else:
            print("Niestety, nie ma takiej opcji")
            input("Enter - Dalej")


    def game(self):
        while True:
            os.system("cls")
            print("""
                =================================
                | 0 - Informacje o zwierzaku    |
                | 1 - Karmienie                 |
                | 2 - Zabawa                    |
                | 3 - Rozmowa                   |
                | 4 - Morderstwo                |
                =================================
            """)

            action = input("Co wybierasz?: ")
            self.choice(action)

if __name__ == '__main__':
    program = Program()
    program.game()
