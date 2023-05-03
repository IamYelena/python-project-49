import prompt

def welcome_user():
    name = ''
    while name == '':
        name = prompt.string('May I have your name?  ')
        print(f'Hello, {name}!')


