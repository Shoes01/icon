class BlankState:
    def __init__(self, mediator):
        self.mediator = mediator

    def render(self):
        print("blank state.")

    def handle_input(self, user_input):
        if user_input == "":
            pass

    def update(self):
        pass