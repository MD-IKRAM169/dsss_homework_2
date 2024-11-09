
import random

def generate_random_integer(min, max):
    """
    Generating a random integer
    """
    return random.randint(min, max)

def generate_random_operator():
    """
    Generating a random arithmetic operator: +/ - / *
    """
    return random.choice(['+', '-', '*'])

def evaluate_expression(num1, num2, operator):
    """
    Evaluate the expression
    """
    expression = f"{num1}  {num2} {operator}"
    if operator == '+': 
        ans = num1 + num2
    elif operator == '-': 
        ans = num1 - num2
    else:
        ans = num1 * num2
    return expression, ans

def math_quiz():
    """
    A math quiz game.
    """
    score = 0
    t_q = 3  # change float to integer.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # changed the value float to int
        operator = generate_random_operator()

        problem, ans = evaluate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_ans = int(input("Your answer: "))
        except ValueError as e:
            print("Invalid input")
            continue

        if user_ans == ans:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ans}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
