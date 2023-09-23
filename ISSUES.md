# Unknowns?
I don't know if the end-of-turn combat and the updates and all that work. Update seems necessary to do combat, but is only called after input is recieved.

# Bad code
[ ] main_screen.py counts the number of tasks per department by comparting the task's category to the menu options. Woof.

# Low Priority Bugs
[ ] SATCOM menu might be wonky... maybe didn't remove a task after completing it? Maybe there's an issue when the task list is longer?
    > Related to the input issue?
[x] When pressing an invalid key, the error is cleared because game.py's run() clears the terminal every loop.

