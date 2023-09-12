from unit import Unit
from typing import List

class Player:
    def __init__(self):
        self.units: List[Unit] = [Unit("soldier")] * 3