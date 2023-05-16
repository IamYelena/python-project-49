import prompt

from random import randint


def generate_questions():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    res1 = generate_question()
    if res1 is False:
        return False
    res2 = generate_question()
    if res2 is False:
        return False
    res3 = generate_question()
    if res3 is False:
        return False
    return True


def generate_question():
    v = randint(0, 100)
    print(f"Question: {v}")
    answer = ''
    while answer == '':
        answer = prompt.string('Your answer:  ')

    r_answer = ''
    if answer == "yes":
        r_answer = "no"
    if answer == "no":
        r_answer = "yes"
    if v % 2 == 0 and answer == "yes":
        print("Correct!")
        return True
    if v % 2 != 0 and answer == "no":
        print("Correct!")
        return True
    r = f"'{answer} is wrong answer ;(. Correct answer was '{r_answer}'."
    print(r)
    return False
