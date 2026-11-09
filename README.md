# Personal Mini-Toolkit

## Project overview
The Personal Mini-Toolkit is a menu-driven Python program with three tools:

1. **Simple Calculator** — adds, subtracts, multiplies, and divides two numbers.
2. **To-Do List Manager** — adds tasks, displays the current list, and removes tasks.
3. **Number Guessing Game** — challenges the user to guess a randomly selected number from 1 to 20.

The program uses variables, input and output, `if` / `elif` / `else`, loops, a changing list, and f-strings. It also checks invalid input and displays friendly messages.

## Files
- `toolkit_plan.txt` — the plan written before coding.
- `toolkit.py` — the complete Python program.
- `screenshots/` — example terminal runs showing the menu and each tool.

## How to run
1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python toolkit.py
   ```

   On some computers, use `python3 toolkit.py` instead.
5. Choose an option from 1 to 4. Choose **4** to quit.

## Testing
The program was checked with an invalid main-menu choice, calculator addition, adding and viewing a to-do task, a completed guessing game, and the Quit option. It also handles invalid numeric input and division by zero without crashing.

## Reflection
The hardest part was making the to-do list menu repeat while still allowing the user to return to the main menu. The bug that took the longest to fix was making sure the task number entered by the user matched the correct list position, because Python lists start counting at zero. I fixed this by checking the entered number and subtracting one when accessing the list. I also tested invalid menu choices and invalid number inputs so the program would not stop unexpectedly. I learned how loops, conditionals, functions, and lists can work together in one program. If I had one more week, I would add a feature that saves tasks to a file so they are still available after the program closes. I would also improve the calculator by adding more mathematical operations.
