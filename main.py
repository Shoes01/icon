from game import Game
from debug_options import DEBUG_ALWAYS_PRINT_FAST, DEBUG_ALWAYS_CLEAR_TEMRINAL


print(f"""
Debug options: 
    {DEBUG_ALWAYS_PRINT_FAST=}
    {DEBUG_ALWAYS_CLEAR_TEMRINAL=}
""")

game = Game()
game.run()