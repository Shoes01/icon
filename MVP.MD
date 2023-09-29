# MVP-XX -- Queueing Tasks
Icon-combat is like when creatures in MTG exchange damage. It is not _the_ battle.
Likewise, The Battle here is not just one icon-combat. 
It is intercepting a UFO, securing a corridor to the site, securing the site itself, setting up command quarters nearby, etc etc.
Each of these "steps" in the battle would have their own forks and obstacles, their own choices to make.
Each time the player "makes a choice", it wastes a turn. 
"Do task" -> wait for new task -> "Do task"
If the player queues tasks, then
"Do task 1/2" -> "Do task 2/2"
But it is riskier, because task 1 may have gone poorly.

# MVP-XX -- Varied Barks
Have more than a few barks per step
Move barks into a .csv file for better maintenance

# MVP-XX -- Different Wincons for Different Icons
Getting 6 wins before 4 losses : already in
Getting X in a row before 4 losses : hmm
Getting X matches more than failures (tug-of-war)
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
How is equipment moved around? Is it permanently tied to a team? 

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

# MVP-XX -- Icon Information
Display icon information for Tasks and Teams.
    These will be discoverable...

# MVP-XX -- Event -> Task -> Team Flow
The main screen will display an event, and the user can "click" on it.
    While on screen, it will just a list of tasks attached to it.
Clicking on a task will display a list of teams that can accomplish the task. 

# MVP-XX -- Standy-By Tasks
Some tasks can be queued up and completed, but they don't "fire" until a condition is met. 
    Example: MEDTEC can be on STANDY_BY for injuries from combat. Once combat is done, the task completes instantly, instead of requiring a turn. 

# MVP-XX -- Combat Upgrade II
The player needs to be able to decide how many icons of each type are on a team.
Or at least reconfigure a team to a pre-set number of icons.

# MVP-XX -- Active Tasks
<!-- 
Are events needed? 
Maybe the tasks are "tied" to events, but the events are only in name. If there are several UFOs on the ground, then the XCOM team would simply have UFO_TASK_1 and UFO_TASK_2, instead of UFO_TASK and then being able to target two events.
But Events might be nice narratively... 
-->
Active tasks target EVENTs.

Need Events.
    Created by passive tasks.
    Targeted by active tasks.
Need to add Events to the display switcher.
Need to remove Events once they are done.
    --> Events are done if all related tasks are completed.
    --> The player may dismiss events. (maybe in the future only)
[?] How are tasks added due to events?
        Are they added once and that's it? Then failing the task generates the same task again? 
        Are the tasks tied to the Event, and tracked somehow? 

# MVP-XX -- Support Tasks II
Issue: teams need to perform the task every turn to maintain support....
    This is because I want the task to always be AVAILABLE,
     which means the combat engine thinks it's always ready to fight.

# [COMPLETE] MVP-08 -- Support Tasks
Some tasks target teams and grants them bonuses.
These tasks are usually ONGOING. 

[x] Subcategories : need to add subcats to all existing tasks.
[x] Consider allowing the UI to work in both directions. Choosing a team -> choosing a task, and choosing a task -> choosing a team.
[x] SUPPORT tasks target a team. 
    Pick task/team --> choose team/task --> choose team that it targets
    (ACTIVE tasks will use this format too, but target an event at the end)
    [ ] Tasks can be done by anyone, and can target any team/event (if support/active). Yes, there will be a lot of bad decisions. XCOM won't do well with SIGINT tasks...
            (if code is already sorting by category, then keep that)
[x] Teams who are being supported don't really need to know. They will gain the icons during combat. They will hold the IDs of the tasks that are supporting them.
    [x] Task is still QUEUED until completed normally
    [x] If the task fails (the team did not have the required icons), it is removed from the team.
    [x] If successful, it becomes ONGOING. 
    [x] It will appear in the task queue or something... for the player to cancel. 
        [x] When cancelled, it clears all the support-related IDs from the task and the supported team.
[?] What kind of support is the team getting? 
    > They can be granted the task's icons
    > They can be granted the team's icons
    [>] They can be granted a set of icons specific to support

__Example__
SATCOM new task: Real-Time Communications. When completed, it targets an XCOM team. 
    This task is ONGOING once it is done. It remains ON_GOING until the player stops it.
    While the task is ONGOING, the XCOM team gets a buff of some sort.
        Perhaps they are granted a few icons during combat.

# [COMPLETE] MVP-07 -- Combat Upgrade
Icons are spent during combat.
A Team with only five A-icons can only match with A-icons five times.
    Might need a special bark for when the icon comes up, but there is "nothing" left.
    I also might need a bark class.

For now, get the icon-dict from the task.
Generate a list. 
Get the icon-dict for the team.
Do combat normally, but deincrement the team's dict with each match.
If there is nothing left, fail match.

How does one win?
1. Getting X matches before Y mismatches -- old way
2. Getting X matches before Y mismatches, but your icons are spent with every match -- current
3. Reducing enemy icons to 0
    > problem: if the enemy has icons you do not, then you can't reduce them. I think this makes it deterministic... 

# [COMPLETE] MVP-06 -- Bark Upgrade
Support a more robust bark system.
    Multiple variations of each bark.
    Support for bark_spent, where a team fails to match an icon because they ran out.

# [COMPLETE] MVP-05 -- Juicy Combat Log
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