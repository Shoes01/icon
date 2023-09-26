from game import Game
import debug_options


print(f"""
Debug options: 
    {debug_options.DEBUG_ALWAYS_PRINT_FAST=}
    {debug_options.DEBUG_ALWAYS_CLEAR_TEMRINAL=}
    {debug_options.DEBUG_ALWAYS_PRINT_STATE=}
    {debug_options.DEBUG_ALWAYS_SHOW_VERBOSE_COMBAT=}
""")

game = Game()
game.run()