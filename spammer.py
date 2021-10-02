import pyautogui as pyauto
import time

time.sleep(5) #You can adjust time.sleep() as per your choice
while True:
    pyauto.write("Hello World") #You can type in whatever message you want to send
    pyauto.press("enter")
    time.sleep(1)
    
#And now you are ready to trouble your friends!!    
