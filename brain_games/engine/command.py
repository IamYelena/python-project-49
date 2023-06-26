import prompt
from brain_games.cli import welcome_user

QUESTION = "Question"
QUESTIONS_COUNT = 3


def run_game(module):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(module.TASK)
    result = True
    for i in range(QUESTIONS_COUNT):
        (question_string, right_answer) = module.generate_question()
        question_string = QUESTION + question_string
        print(question_string)
        user_answer = prompt.string('Your answer:  ')
        if str(user_answer) == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'. ")
            result = False
            break

    if result is True:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + "!")
