"""
Personal Mini-Toolkit
A menu-driven program containing a calculator, a to-do list, and a guessing game.
"""

import random


def simple_calculator():
    # This tool performs addition, subtraction, multiplication, and division.
    print("\n--- SIMPLE CALCULATOR ---")
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            answer = first_number + second_number
        elif operator == "-":
            answer = first_number - second_number
        elif operator == "*":
            answer = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
                return
            answer = first_number / second_number
        else:
            print(f"'{operator}' is not a supported operation.")
            return

        print(f"Your answer is: {answer:g}")
    except ValueError:
        print("Please enter valid numbers. The calculator needs numeric input.")


def todo_list_manager(tasks):
    # This tool lets the user add, view, and remove tasks in a changing list.
    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task you want to add: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number is not on the list.")
                except ValueError:
                    print("Please enter a whole number.")
        elif choice == "4":
            print("Returning to the main menu...")
            break
        else:
            print("That option is not available. Please choose 1, 2, 3, or 4.")


def number_guessing_game():
    # This tool asks the player to guess a random number and gives helpful hints.
    print("\n--- NUMBER GUESSING GAME ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    print("I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Please choose a number from 1 to 20.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Correct! You guessed the number in {attempts} attempt(s).")
                break
        except ValueError:
            print("Please enter a whole number.")


def main():
    # The main loop keeps showing the menu until the user chooses Quit.
    tasks = []

    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n========== PERSONAL MINI-TOOLKIT ==========")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list_manager(tasks)
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
