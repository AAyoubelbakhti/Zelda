
prompt = [""] * 8


def clearPrompt():
    global prompt
    prompt = [""] * 8

def addToPrompt(text):
    global prompt
    prompt.append(text)
    if len(prompt) > 8:
        prompt.pop(0)

def drawPrompt():
    global prompt
    for text in prompt:
        print(text)

