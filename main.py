import random
import time
import sys
import os

def choice ():
  choices =  ['7','🍋','🍒','🍊','🍇','🍉','🍌','🍓','bar','wild','jackpot']
  choice_main = random.randint(0,7)
  choice_higher = random.getrandbits(1)
  if choice_higher == 1:
    add = random.randint(1,3)
    choice_main += add
  return choice_main

def get_values():
  choice1 = choice ()
  choice2 = choice ()
  choice3 = choice ()

def main ():
  choices =  ['7','🍋','🍒','🍊','🍇','🍉','🍌','🍓','bar','wild','jackpot']
  choice_main = random.randint(0,10)
  print