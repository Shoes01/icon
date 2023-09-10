import sys

introduction: str =\
"""
Welcome to $game.
Press N for new game.
Press Q to quit.
"""

print(introduction)

while True:
    choice: str = input(">>> ")
    if choice == "N":
        print("Starting new game...")
        print("<code the rest of the game...>")
    elif choice == "Q":
        print("Quitting...")
        sys.exit()
    else:
        print("Invalid choice.")
        print(introduction)

        
