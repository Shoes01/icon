# MVP-XX -- Varied Barks
Have more than a few barks per step

# MVP-XX -- Different Wincons for Different Icons
Getting 6 wins before 4 losses : already in
Getting X in a row before 4 losses : hmm
what's more fun?
This could mean that some icons would mix better together?

# MVP-XX -- "Real Time"
The game is real time, in the same way OG Xcom was real time. 
Tasks take X hours, and "ending the turn" either skips a day, or skips to the next finished task, or something.

# MVP-XX -- Equipment
Some icons are granted by training, some are granted by equipment
To create a new team, the player needs the required equipment.
Research or Salvage would allow the player to collect and make equipment. 
    Research gives new icons so that salvage can get more out of wreckage.
    Salvage actually gets things out of wreckage sites.

# MVP-XX -- HR and Hiring Teams
New department: HR. 
Allow the creation of new Teams. 
    It ..could.. use the icon combat system. But that's a bit silly. 
        Maybe it's a 100% winchance, and the barks are very boring filling out forms and whatnot. 
    Eventually though.. advanced teams could require advanced icons, acquired through curriculum development..

# MVP-XX -- Linear Progress Barks, and Dynamic Barks
Some tasks are linear (like the SIGINT task). Barks are in a specific order.
Some tasks are not linear (like XCOM combat tasks). These barks should be icon-specific. 
    Would they be task _and_ icon specific? They could be... so an Attack icon would generate different barks on a scout UFO vs a battleship UFO

# MVP-XX -- Multi-Icon Steps
Some steps in tasks require two icons to be successful. 
    Generally, this is harder.
Maybe succeeding this task gives a bonus of some sort.
    (Crying Suns allowed you to loot, and thus gain equipment)

# MVP-XX -- Tasks Change Over Time
Some tasks should gain difficulty over time, representing fortifications and reinforcements.
The task could have an age, and depending on the age could be the added tasks.
And after an amount of time, the task expires.
    This could also generate new tasks. 

# MVP-XX -- Multi-Team Tasks and Task-Icon Manipulation
<!-- Is this a subset of on-going tasks? -->
When a team queues a task, other teams may lend support. 
    The support may succeed or fail.
        If they succeed, an icon is added to the Task
        or, an icon is added to the Team _temporarily_.
At some point, the player then executes the task.

Support tasks are always seeable, but are greyed out with a "supports task X".
    If that task is queued, then the task is available.

This means the player first picks a team, then a task. The queue is set.
    This queues task now appears in the task-list of other teams.
Then, the player enters a new menu and either cancels the task, or executes it.

## Example
    A new task Crashed UFO appears.
    A RECON team can complete the Reconnaissance Task, revealing which icons are present.
    A ENGIN team can complete the Combat Support Task, adding an Artillery icon to the task.
        The XCOM team will only benefit from this if they've been trained to make use of Artillery. 
        Otherwise, it is a neutral task - not a failure. Unless I want it to be a failure task lol.
    A SATCOM team can complete the Real-Time Datastream, adding a Flanking icon to the task.
    A BIOTECH team can complete the Muton Briefing, removing the Muton icons from the task, if any.
        Or, the icon is temporarily added to the XCOM team. This can provide a nice bark :)

# MVP-XX -- Stand-by Tasks
Some tasks can be put on stand-by.
The moment they are eligible to be done, they are done.
    on-going tasks are cancelled to perform this
    in-progress tasks are completed before performing this.

# MVP-XX -- Cooldown Icons
Instead of going on cooldown, some teams can gain temporary icons.
These icons can be removed by specific tasks. 
    Example: 

# MVP-XX -- On-Going Tasks II
These also apply to "friendly teams".
    Example: ACADEMY has a task Sectiod Theory, and it grants the XCOM team a Section Icon for the duration of the task.
Teams would need to have a limited amount of "slots", representing how much time in a day they have to train. 
    When they are on cooldown, they lose all bonus icons.
    _or cooldown adds bad icons that need to be cleared through R&R..?_

# MVP-XX -- On-Going Tasks
Some tasks, once completed, continue to give its bonus. 
    I guess this would be support tasks. Roll it, succeed or not, and then it stays ON_GOING until the task it is attached to is complete.
Other tasks, such as some generic SIGINT task scanning frequencies, could be required to generate new tasks.
    SIGINT task: listen for UFOs. While active, gives a +10% chance to detect a UFO.
    SATCOM taks: active surveillance. While active, gives a +10% chance to find a window of opportunity in an attack. 

# MVP-XX -- Multi-Stage Tasks
Some tasks are multi-stage. When one stage is complete, the player is prompted with completing the next one right away.
    If they decline, the task disappears.

# MVP-XX -- Task Discoverability
Task Icons are hidden.
    If an icon is successfully matched, then it becomes discovered. 
    Otherwise, it remains hidden.
    Also need to track which icons are _not_ in the task, as the player tries it.

Task wincons and losecons are also hidden until discovered. 

Eventually, I want the player to attempt tasks to see what sort of Icons they require.
(This could done via RECON - a dummy team who simply runs the icons, fails them all, and gets put on cooldown)

# MVP-06 -- Icon Information
Display icon information for Tasks and Teams.
    These will be discoverable...

# [COMPLETED] MVP-05 -- Juicy Combat Log
"Beginning this thing..." then roll if it succeeds or not. Then bark the win or the loss. J U I C Y

# [COMPLETE] MVP-04 -- Task Queue and Execution
Change workflow so that tasks are QUEUED. 
Ending the turn executes all QUEUED tasks.
QUEUED tasks may be returned to AVAILABLE.
Teams and Tasks have IDs. 

# [COMPLETE] MVP-03 -- Task Engine
Need to support a task creating new tasks.
I almost already have this done. But I want to formalize it inside the task, not in the code. 
    And as a list.

# [COMPLETE] MVP-03 - Live Terminal
Print the combat text out gradually, for juice

# [COMPLETE] MVP-02
Improve the narrative of "combat".

# [COMPLETE] MVP-01
Need to add icons to Task and Team
Need to use icons in combat - start simple: if all icons match, win. Else, lose.