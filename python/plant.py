from sys import exit
from time import sleep
from Adafruit_MPR121 import MPR121
import pygame.mixer
from glob import glob
import random

cap = MPR121.MPR121()
pygame.mixer.init()

jokes = [pygame.mixer.Sound(sound) for sound in glob("jokes/*.wav")]

def main():
    last_touched = cap.touched()
    while True:
        current_touched = cap.touched()
        for i in range(12):
            pin_bit = 1 << i
            if current_touched & pin_bit and not last_touched & pin_bit:
                print('%s touched!' % i)
                sound = random.choice(jokes)
                sound.play()
        last_touched = current_touched
        sleep(0.1)

if __name__ == '__main__':
    if not cap.begin():
        print('Error initializing MPR121.  Check your wiring!')
        exit(1)
    else:
        main()
