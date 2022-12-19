import pyautogui as code
import pywhatkit as kit
import time

limit = input ("enter n° of messsage ")
Message = input("Message you want to send ")

i=0

time.sleep(8)

while i<int(limit):
    code.typewrite(Message)
    code.press("Enter")
    i+=1
