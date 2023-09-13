class PlayState:
    def __init__(self, mediator):
        self.mediator = mediator

    def render(self):
        unit_list = ""
        for unit in self.mediator.game.player.units:
            unit_list += unit.name
            unit_list += ", "
        unit_list = unit_list[:-2]

        task_list = ""
        for task in self.mediator.game.task_stack:
            task_list += task.category.upper() + " (" + task.name.title() + ")"
            task_list += ", "
        task_list = task_list[:-2]
        if len(task_list) == 0:
            task_list = "None"
        

        print(
f"""
PLAY STATE

Your available force are: {unit_list}.

Tasks available: {task_list}.

1. Prepare attack. 
2. Pass the turn.
"""
        )

    def handle_input(self, user_input):
        if user_input == "1":
            self.mediator.change_state(self.mediator.attack_state_1)
        elif user_input == "2":
            self.mediator.end_turn()

    def update(self):
        pass