# Taks Chain 1
<!-- EVENTs will generate TASKs, which can be completed by teams. -->
<!-- Completing a TASK by generate more TASKs, or a new EVENT. -->
SIGINT: Surveillance.
>> New Event: Alien Signal Detected.
    >> New Task - SIGINT: Identify Source \\get a location
    >> New Task - SIGINT: Analyze Signal \\get info from it
SIGINT: Signal Tracking
--> New Task: Investigate Source

# Sept 23 notes
In MTG, combat is actually super simple: if power > toughness, the creature dies.
In this game, the icon-combat is similarly simple. 
The complexity/fun arises in all things surrounding combat.

I should create a number of "stories" on which to base my missions
Departments need "passive" tasks to do when there is "nothing" to do.
    --> This does not really need to be planned out.
# Sept 11 notes
## Task Engine
There should be a list of tasks that is unknown to the player. 
    Example: SIGINT starts "scanning". The game looks through the task list and picks one at random. A few icons are tested to see if the signal is traceable. If so, a new task is added that SIGINT can study. If the icon-combat is unsuccessful, the task remains.
Some tasks are known to the player.
Some tasks expire after a given amount of time.
Most tasks lead to more tasks.
    Either when they expire, or when they are "completed".
## Combat Engine
Two units are fed into the combat function.
The attacker has a static list of icons.
The defender has a generated "pattern of events", made up from its list of icons.
One by one, each icon from this pattern is compared to the attacker.
    If the icon is found in the list of icons from the attacker: success
    else: fail
Simple version: if all icons match, success.
# Sept 10 notes
## Example of flow
SIGINT will listen for signals
They will track them.
It will use the ICON mini game. 
There are rewards for getting to X% completion. 
One of the rewards is creating a task for SATCOM to look at a site for the UFO.
Finding it creates tasks for XCOM, RECON, STRIKECOM.
Each task has its own set of icons etc, completing it generates tasks for other departments. Culminating in some SCAVENGE team going in
