import pyautogui
import time

text = input('What is he message that you want to send?:')
n = input('How many times should I send this message?:')

print("IMMA CHARGIN' MAH LASER...")

c = 5
while c != 0:
    print(c)
    time.sleep(1)
    c -= 1

print("FLOODING NOW...")

for n in range(0, int(n)):
    pyautogui.typewrite(text + '\n')
