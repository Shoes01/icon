import sys
import logging
import log_config
from game import Game

log_config.configure_logging()
log: logging.Logger = log_config.get_logger(__name__)
log.info("Begin script.")

print(
"""
Welcome to 

  _____ _____ ____  _   _          __    _____  ______      ________ _____  _   _ __  __ ______ _   _ _______ 
 |_   _/ ____/ __ \| \ | |        / _|  / ____|/ __ \ \    / /  ____|  __ \| \ | |  \/  |  ____| \ | |__   __|
   | || |   | |  | |  \| |   ___ | |_  | |  __| |  | \ \  / /| |__  | |__) |  \| | \  / | |__  |  \| |  | |   
   | || |   | |  | | . ` |  / _ \|  _| | | |_ | |  | |\ \/ / |  __| |  _  /| . ` | |\/| |  __| | . ` |  | |   
  _| || |___| |__| | |\  | | (_) | |   | |__| | |__| | \  /  | |____| | \ \| |\  | |  | | |____| |\  |  | |   
 |_____\_____\____/|_| \_|  \___/|_|    \_____|\____/   \/   |______|_|  \_\_| \_|_|  |_|______|_| \_|  |_|   

Press "q" to return to previous state.
Press "x" to quit.
"""
)


game = Game()
game.run()

print("\nGoodbye.\n")