
prompt = [""] * 8


def clear_prompt():
    global prompt
    prompt = [""] * 8

def add_to_prompt(messages):
    global prompt
    for message in messages:
        if isinstance(message, str):
            prompt.append(message)
        else:
            add_to_prompt(message)

def draw_prompt():
    global prompt
    print('\n'.join(prompt))
