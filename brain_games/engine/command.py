import prompt
from brain_games.cli import welcome_user

QUESTIONS_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.TASK)
    for i in range(QUESTIONS_COUNT):
        (question_string, right_answer) = game.generate_question()
        question_string = f"Question: {question_string}"
        print(question_string)
        user_answer = prompt.string('Your answer:  ')
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'. ")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
