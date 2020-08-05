import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    name = 'Bart'

    def __init__(self):
        self.score = 0
        self.history = ['scissors', 'paper']
        # History used to be randomly initialised but this could result
        # in a infinite tie break combining an always player with a
        # reflect player

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.history = [my_move, their_move]


# Plays a random move
class randomPlayer(Player):
    name = 'Rango'

    def move(self):
        return random.choice(moves)


# Plays a move that wasn't just used
class unrepeatPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Dodger'

    def move(self):
        while True:
            randmove = random.choice(moves)
            if randmove not in self.history:
                return randmove


# Asks user for input
class humanPlayer(Player):
    name = "User"

    def move(self):
        while True:
            # usermove = input("Rock, paper, or scissors? ")
            usermove = input("Rock, paper, scissors, lizard or spock? ")
            if 'q' in usermove:
                return usermove
            if usermove in moves:
                return usermove


# Plays the move the opponent last used
class reflectPlayer(Player):
    name = 'Anna'

    def move(self):
        return self.history[1]


# Runs through the options in order
class cyclePlayer(Player):
    name = 'Lance'

    def move(self):
        previous = moves.index(self.history[0])
        try:
            return moves[previous+1]
        except IndexError:
            return moves[0]


# Always plays spock
class trekkiePlayer(Player):
    name = 'Kirk'

    def move(self):
        return('spock')


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def silent_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if ('q' in move1 or 'q' in move2):
            self.game_end()
        points = shhresult(move1, move2)
        self.p1.score += points[0]
        self.p2.score += points[1]
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if ('q' in move1 or 'q' in move2):
            self.game_end()
        print(f"{self.p1.name} played {move1}")
        print(f"{self.p2.name} played {move2}")
        print('')
        points = result(move1, move2)
        print('')
        self.p1.score += points[0]
        self.p2.score += points[1]
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Scores: {self.p1.name} {self.p1.score},"
              f" {self.p2.name} {self.p2.score} \n")

    def game_end(self):
        print("Game Over")
        if self.p1.score > self.p2.score:
            print("You are the winner!!!")
        elif self.p2.score > self.p1.score:
            print("You Lost! The takeover has begun, Mwa ha ha ha!!")
        else:
            print("I guess we can be called equals now ;) ")
        again()

    def gamemode(self):
        print("Which game mode would you like?")
        print("Press 1 for 'Best of' mode")
        print("Press 2 for 'Win by' mode")
        print("Press 3 for 'Endless' mode")
        print("or press 'q' to exit: ")
        while True:
            x = input("")
            if x in ['1', '2', '3']:
                return x
            elif 'q' in x:
                quit()
            else:
                print("Please enter 1, 2, 3 or 'q' ")

    def best_of(self, rounds):
        for round in range(rounds):
            if (
                 isinstance(self.p1, humanPlayer) or
                 isinstance(self.p2, humanPlayer)
                 ):
                print(f"Round {round}:")
                self.play_round()
            else:
                self.silent_round()

    def win_by(self):
        scorediff = getnum("How many would you need to win by? ")
        while (self.p1.score - self.p2.score) < scorediff:
            self.play_round()

    def endless(self):
        while True:
            self.play_round()

    def play_game(self):
        print("Game start!")
        self.mode = self.gamemode()
        if self.mode == '1':
            rounds = getnum("How many rounds would you like? ")
            self.best_of(rounds)
        elif self.mode == '2':
            self.win_by()
        else:
            self.endless()
        self.game_end()


class tournament:
    def __init__(self, players):
        self.starters = []
        random.shuffle(players)
        self.starters = players
        self.semis = []
        self.finalists = []

    def begin(self):
        print("The tournament is played in a knockout fashion")
        print("Each match is decided by the best of 7 rounds")
        print("The first round matches are as follows")
        for num in range(1, 5):
            print(f"Match {num}: {self.starters[num-1].name} vs "
                  f"{self.starters[num+3].name}")
        self.firstround()
        self.semifinals()
        self.finals()

    def suddendeath(self,  match):
        print("Its a tie, We have gone to sudden death!!!")
        while match.p1.score == match.p2.score:
            match.play_round()

    def playmatch(self, p1, p2):
        match = Game(p1, p2)
        match.best_of(7)
        if p1.score == p2.score:
            self.suddendeath(match)
        if p1.score > p2.score:
            return p1
        else:
            return p2

    def firstround(self):
        print("Let us begin")
        for num in range(4):
            print(f"{numbers[num]} match: {self.starters[num].name} vs"
                  f" {self.starters[num+4].name} ")
            winner = self.playmatch(self.starters[num], self.starters[num+4])
            winner.score = 0
            self.semis.append(winner)
            print(f"{winner.name} wins and moves into the Semi-finals\n")

    def semifinals(self):
        print("That was a hectic opening round! Now onto the semi-finals!!")
        print("The matches are: \n")
        print(f"{self.semis[0].name} vs {self.semis[2].name}")
        print(f"{self.semis[1].name} vs {self.semis[3].name}")
        for num in range(2):
            print(f"{numbers[num]} Semi-final: {self.semis[num].name} vs"
                  f" {self.semis[num+2].name} ")
            winner = self.playmatch(self.semis[num], self.semis[num+2])
            winner.score = 0
            self.finalists.append(winner)
            print(f"{winner.name} wins and moves into the Finals\n")

    def finals(self):
        print("Wow, that was intense. now for the moment you've "
              "all been waiting for...")
        print(f"The Final showdown between {self.finalists[0].name}"
              f" and {self.finalists[1].name}!!!")
        champion = self.playmatch(self.finalists[0], self.finalists[1])
        print(f"After that great excitement {champion.name} "
              f"is crowned victorious")
        again()


def beats(one, two):  # Returns True if one beats two
    return (
            (one == 'rock' and two in ['scissors', 'lizard']) or
            (one == 'scissors' and two in ['paper', 'lizard']) or
            (one == 'paper' and two in ['rock', 'spock']) or
            (one == 'lizard' and two in ['spock', 'paper']) or
            (one == 'spock' and two in ['scissors', 'rock'])
            )


def shhresult(one, two):
    if one == two:
        return [0, 0]
    elif beats(one, two):
        return [1, 0]
    else:
        return [0, 1]


def result(one, two):
    if one == two:
        print("Its a Tie")
        return [0, 0]
    elif beats(one, two):
        print(f"{one} beats {two}")
        return [1, 0]
    else:
        print(f"{two} beats {one}")
        return [0, 1]


def getnum(query):
    while True:
        try:
            return int(input(query))
        except ValueError:
            print("Please enter a number")


def gamestyle():
    print("Would you like to?")
    print("1. Play a single game,")
    print("2. Participate in a tournament")
    print("3. Run for your life")
    style = getnum("")
    if style in [1, 2]:
        return style
    elif style == 3:
        print("You can run but you can't hide!!")
        quit()


def again():
    if 'y' in input("Would you like to play again? "):
        rungame()
    else:
        quit()


def rungame():
    print("This is a rock paper scissors game")
    style = gamestyle()
    players = [Player(), randomPlayer(), reflectPlayer(),
               cyclePlayer(), unrepeatPlayer(), trekkiePlayer()]
    if style == 1:
        cpu = random.choice(players)
        game = Game(humanPlayer(), cpu)
        game.play_game()
    else:
        # extra random player to make 8
        players.extend([humanPlayer(), randomPlayer()])
        tourny = tournament(players)
        tourny.begin()


numbers = ['First', 'Second', 'Third', 'Fourth']
moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
# moves = ['rock', 'paper', 'scissors']

if __name__ == '__main__':
    rungame()
