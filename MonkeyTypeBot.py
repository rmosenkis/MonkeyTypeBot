import random
import string
import time

import keyboard as kb
from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()),options = options)

new_string = ""

intext = input("Enter 1 to load MonkeyType.\nEnter 2 to load TypeRacer.\n")
if intext == "2":
    driver.get('https://play.typeracer.com/')
else:
    driver.get('https://monkeytype.com/')

input("Hit enter once page is loaded.\n")
sleep = 0.00025
sleepHalf = sleep / 2

if intext == "2":
    words = driver.find_elements(By.CSS_SELECTOR,'table.inputPanel')
    new_string = words[0].get_attribute('textContent')
else:
    words = driver.find_elements(By.CLASS_NAME,'word')
    new_array = words
    for i in range(len(words)):
        new_array[i] = words[i].get_attribute('textContent')
    for word in new_array:
        new_string += word + " "

print(f"Press enter to start")
time.sleep(1)
typeKey = Controller()
while not kb.is_pressed('enter'):
    time.sleep(0.01)
time.sleep(3)

for char in new_string:
    """
    if random.randint(0,10) <= 1:
        for x in range(random.randint(1,2)):
            random_char = random.choice(string.ascii_letters)
            typeKey.press(random_char)
            time.sleep(sleepHalf)
            typeKey.release(random_char)
            time.sleep(sleepHalf)
            typeKey.press(Key.backspace)
            typeKey.release(Key.backspace)
    """
    typeKey.press(char)
    typeKey.release(char)
    time.sleep(sleep)