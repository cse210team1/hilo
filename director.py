from dealer import Dealer
class Director

    def __init__(self):
            """The class constructor.
            
            Args:
                self (Director): an instance of Director.
            """
            self.keep_playing = True
            self.score = 0
            self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        print(f"The card is : {self.dealer.current_card}" )
        higher_lower = input("Higher or lower? [h/l] ")
        
        
    def do_updates(self):
        self.dealer.draw_card()
        
        if higher_lower == "h":
            if self.dealer.compare_to_last_card == "h"
            self.score += 100
        elif higher_lower == "l":
            if self.dealer.compare_to_last_card == "l"
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        print(f"Your score is: {self.score} ")
        if self.score > 0 
            choice = input("Keep playing? [y/n] ")
        self.keep_playing = (choice == "y")
