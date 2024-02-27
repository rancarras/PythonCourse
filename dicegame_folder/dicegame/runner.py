# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:21:15 2024

@author: ranca
"""

from .die import Die
from .utils import error

class GameRunner:

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0 
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        runner = cls()    
        runner.reset()
        while True:
            runner.dice = Die.create_dice(5)
            print("Round {}\n".format(runner.round))

            for i in runner.dice:
                print(i.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1
            
            if runner.wins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break
            elif runner.wins <= 6:
                pass
            else:
                print("You lost! Start the game again to play it once more")
                runner.reset()
                pass

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                pass
            elif prompt == 'n' or prompt == 'N':
                break
            else:
                error()
                break