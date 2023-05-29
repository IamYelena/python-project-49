def welcome():
    print("Welcome to the Brain Games!")


def final_message(result, name):
    if result is True:
        print("Congratulations, " + name + "!")
    else:
        print("Let's try again, " + name + "!")


def proccessing_result(user_answer, right_answer):
    if str(user_answer) == str(right_answer):
        print("Correct!")
    else:
        print(f'Your answer:  {user_answer}')
        print(f"'{user_answer}' is wrong answer ;(."
              f" Correct answer was '{right_answer}'. ")

    if str(user_answer) == str(right_answer):
        return True
    else:
        return False