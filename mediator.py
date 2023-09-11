from states.main_menu_state import MainMenuState
from states.play_state import PlayState
from states.settings_state import SettingsState
from states.battle_state import BattleState

class Mediator:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.main_menu_state = MainMenuState(self)
        self.play_state = PlayState(self)
        self.settings_state = SettingsState(self)
        self.battle_state = BattleState(self)

    def change_state(self, new_state):
        self.state_machine.change_state(new_state)
    
    def previous_state(self):
        self.state_machine.previous_state()