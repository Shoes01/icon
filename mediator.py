from states.main_menu_state import MainMenuState
from states.play_state import PlayState
from states.settings_state import SettingsState
from states.battle_state import BattleState
from states.attack_state import AttackState

class Mediator:
    def __init__(self, game):
        self.game = game
        self.main_menu_state = MainMenuState(self)
        self.play_state = PlayState(self)
        self.settings_state = SettingsState(self)
        self.battle_state = BattleState(self)
        self.attack_state = AttackState(self)

    def change_state(self, new_state):
        self.game.change_state(new_state)
    
    def previous_state(self):
        self.game.previous_state()