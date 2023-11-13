
import random


def generate_random_integer(minimum, maximum):
    """
    Returns a random integer between minimum and maximum (inclusive).
    """
    return random.randint(minimum, maximum)


def generate_random_operator():
    """
    Returns a random operator from the list ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(num1, num2, operator):
    """
    Returns a tuple containing a string problem and an integer answer.
    The string problem is a formatted string that concatenates num1, operator, and num2.
    The integer answer is the result of the arithmetic operation between num1 and num2 based on the operator.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Generates a math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()