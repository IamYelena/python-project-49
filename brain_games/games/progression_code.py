import prompt

from random import randint, randrange

def generate_questions():
    print("What number is missing in the progression?")
    res1 = generate_question()
    if res1 == False:
        return False
    res2 = generate_question()
    if res2 == False:
        return False
    res3 = generate_question()
    if res3 == False:
        return False
    return True
    
def generate_question():
    start_number = randint(1,10)
    step = randint(1,10)
    number_hidden_element = randint(0,9)
    array = []
    for number in range(0,10):
        element = start_number + number*step
        array.append(element)
    
    hidden_element = array[number_hidden_element]
    right_answer = hidden_element
    array[number_hidden_element] = ".."
    
    query_string =  ""
    for element in array:
        query_string = query_string + str(element) + " "
    query_string = query_string.strip()
    print(f"Question: {query_string}")
    user_answer = ''
    while user_answer == '':
        user_answer = prompt.string('Your answer:  ')
    
    print_result(user_answer,right_answer)

    if str(user_answer) == str(right_answer):
        return True
    else:
        return False
            
    return False
    
def print_result(user_answer,right_answer):
    if str(user_answer) == str(right_answer):
        print("Correct!")
    else:
        print(f'Your answer:  {user_answer}')
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'. ")