import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        move = ""
        while move not in moves:
            move = input("rock, paper or scissors? ").lower()
        return move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = "none"

    def move(self):
        if "none" == self.next_move:
            self.next_move = random.choice(moves)
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(ReflectPlayer):
    def learn(self, my_move, their_move):
        self.next_move = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }[my_move]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.rounds = 1
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move2, move1)
        print(f"\nHUMAN plays {move1}, ME plays {move2}", end=", ")
        if move1 == move2:
            print("TIE!")
        elif beats(move1, move2):
            print("HUMAN WINS!")
            self.score_p1 += 1
        else:
            print("ME WINS!")
            self.score_p2 += 1
        print(f"human: {self.score_p1}  me: {self.score_p2}")

    def play_game(self):
        rounds = 0
        while rounds not in range(1, 10):
            rounds = int(input(f"\nHow many rounds human? (1-9)\n"))
        for round in range(rounds):
            print(f"\nRound {round+1}/{rounds}")
            self.play_round()
        print(f"\nFINAL SCORE: HUMAN: {self.score_p1}  ME: {self.score_p2}")
        if self.score_p1 < self.score_p2:
            print("ME WIN, YOU LOSE!")
        elif self.score_p1 > self.score_p2:
            print("Lucky human, I'll beat you next time")
        else:
            print("Good moves, it was a tie")


def pick_opponent():
    opponents = {
        "zoe": RandomPlayer(),
        "mark": ReflectPlayer(),
        "dave": CyclePlayer()
    }
    choice = "none"
    while choice not in opponents:
        choice = input("Choose your DOOM: Zoe, Mark or Dave?\n").lower()
    return opponents[choice]


if __name__ == '__main__':
    game = Game(HumanPlayer(), pick_opponent())
    game.play_game()
