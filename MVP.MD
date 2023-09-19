# MVP-XX -- Task Icon Discoverability
Eventually, I want the player to attempt tasks to see what sort of Icons they require.
(This could done via RECON - a dummy team who simply runs the icons, fails them all, and gets put on cooldown)

# MVP-02
Improve the narrative of "combat".

One task has different levels of completion.
Once one step is completed, the player has a chance to continue or stop.

Failing to match X icons means you lose the current step.
Failed icons don't reset for the next step -- they accumulate.
The team is put on cooldown for as many turns as they have mismatched icons
--> this means pushing your luck and failing a step wastes turns.

Each step would have to give its own reward... 

Also include "neutral" icons, that do not count as a loss when they are failed to match --> they only add to the narrative... 

BUG: I don't think the win barks and fail barks match up
BUG: Sanitation of user input is wonky with double columns... 

## Detour
On SIGINT screen, show teams in detail, including cooldowns. 
Also show tasks...  do I need columns???

Show both columns. Darken the one not necessary. 
Choose task.
Highlight task, darken the others, and regular_print the teams. 
Choose team.
(Ask an "are you sure" prompt ig)

I can use padding to help with this.

```py
def print_two_columns(tasks: List[Task], teams: List[Team], printer): # what is the type of printer? 
    menu_length = max(len(teams), len(tasks))

    for i in range(menu_length):
        team = "" if len(teams) < i else teams[i].name
        task = "" if len(tasks) < i else tasks[i].name

        left_col = f"{i+1}. {task}"
        right_col = f"{i+1}. {team}"
        printer(left_col.ljust(20) + right_col)

```


# MVP-01
Need to add icons to Task and Team
Need to use icons in combat - start simple: if all icons match, win. Else, lose.

## old mvps vvv
# MVP-06 - Task Engine II
After the combat task, a cleanup task is generated.
    "Cleanup" also uses the combat engine. Just with differen units, and thus different icons.
# MVP-05 - Task Engine
When the game starts, there will be no task.
After the first turn, a "combat task" will appear.
