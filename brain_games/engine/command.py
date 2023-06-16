import prompt


def welcome():
    print('Welcome to the Brain Games!')


def final_message(result, name):
    if result is True:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + "!")


def proccessing_result(user_answer, right_answer):
    if str(user_answer) == str(right_answer):
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f" Correct answer was '{right_answer}'. ")

    if str(user_answer) == str(right_answer):
        return True
    else:
        return False


def run_game(QUESTIONS_COUNT, generate_question):
    for i in range(QUESTIONS_COUNT):
        (question_string, right_answer) = generate_question()
        print(question_string)
        user_answer = prompt.string('Your answer:  ')
        res1 = proccessing_result(user_answer, right_answer)
        if res1 is False:
            return False
    return True
