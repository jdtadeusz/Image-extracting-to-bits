import cv2
import os
import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import image
import sys
import others

url = 'https://raw.githubusercontent.com/vision-agh/poc_sw/master/02_Point/'
fileName = '100zloty.jpg'


image.imageImport(url, fileName)

d = image.imageExtracting(fileName)


if d:
    image.displayBits(d)
    while True:
        print(f"\nCzy chcialbys zrekonstruowac obraz z danej ilosci bitow?\n1. Tak\n2. Nie")
        try:
            choice = int(input(": "))
            if choice == 1:
                while True:
                    try:
                        others.clearConsole()
                        bits_num = int(input("Z ilu bitow chcialbys zrekonstruowac obraz? (1-8)\n\n: "))
                        if 0 < bits_num <= 8:
                            image.reconstructImage(d, bits_num)
                            break
                        else:
                            print("Niepoprawna liczba bitow.\nWcisnij enter by sprobowac ponownie.")
                            input()
                            others.clearConsole()

                    except ValueError:
                        print("Wprowadz liczbe calkowita z przedzialu <1,8>")
            elif choice == 2:
                sys.exit()
            else:
                sys.exit()
            break
        except ValueError:
            print("Wprowadz liczbe calkowita z przedzialu <1,2>\nWcisnij enter by sprobowac ponownie.")
            input()
            others.clearConsole()

