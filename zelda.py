import os
import platform
import random

def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def clearPrompt():
    global prompt
    prompt = [""] * 15

def addToPrompt(text):
    global prompt
    prompt.append(text)
    if len(prompt) > 15:
        prompt.pop(0)

def drawPrompt():
    global prompt
    for text in prompt:
        print(text)