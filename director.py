from dealer import Dealer
class Director:

    def __init__(self):
            """The class constructor.
            
            Args:
                self (Director): an instance of Director.
            """
            self.keep_playing = True
            self.score = 300
            self.dealer = Dealer()
            self.higher_lower = None

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print(f"Your score is: {self.score} ")
        print(f"The card is: {Director.display(self.dealer.current_card)}" )
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        self.higher_lower = input("Will the next card be higher or lower? [h/l] ")
        
        
    def do_updates(self):
        self.dealer.deal_card()
        if self.higher_lower == self.dealer.compare_to_last_card():
            self.score += 100
        else:
            self.score += -75

    def do_outputs(self):
        print(f"The card is: {Director.display(self.dealer.current_card)}" )
        print(f"Your score is: {self.score} ")

        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else: 
            print("You lose")
            self.keep_playing = False

    @staticmethod
    def display(card):
        if card == 1:
            display = "A"
        elif card == 11:
            display = "J"
        elif card == 12:
            display = "Q"
        elif card == 13:
            display = "K"
        else:
            display = card

        return display