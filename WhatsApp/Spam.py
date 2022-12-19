import pyautogui as spam
import time

limit = input("enter your limit: ")
Message = input("enter your message: ")

i = 0

#using while loop in this project

time.sleep(10)

while i<int(limit):
    spam.typewrite(Message)
    spam.press('Enter')

    i+=1

