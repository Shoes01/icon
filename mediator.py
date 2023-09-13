from states.main_menu_state import MainMenuState
from states.play_state import PlayState
from states.settings_state import SettingsState
from states.attack_step_1_state import AttackState_1
from states.attack_step_2_state import AttackState_2

class Mediator:
    def __init__(self, game):
        self.game = game
        self.main_menu_state = MainMenuState(self)
        self.play_state = PlayState(self)
        self.settings_state = SettingsState(self)
        self.attack_state_1 = AttackState_1(self)
        self.attack_state_2 = AttackState_2(self)

    def change_state(self, new_state):
        self.game.change_state(new_state)
    
    def previous_state(self):
        self.game.previous_state()
    
    def end_turn(self):
        self.game.end_turn()