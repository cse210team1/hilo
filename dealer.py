import random

class Dealer():

    def __init__(self):
        self.current_card = random.randint(1, 13)
        self.last_card = random.randint(1, 13)

    def deal_card(self):
        self.last_card = current_card
        self.current_card = random.randint(1, 13)

    def compare_to_last_card(self):
        if self.current_card > self.last_card:
            return "h"
        elif self.current_card < self.last_card:
            return "l"
        else:
            return "e"
