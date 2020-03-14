class CricketStats:
    def __init__(self, first, last, runs, balls, matches):
        self.first = first
        self.last = last
        self.runs = runs
        self.balls = balls
        self.matches = matches

    def fullname(self):
        return f'{self.first} {self.last}'

    def stats(self):
        return f'{self.first} {self.last} scored {self.runs} of {self.balls} balls'

    def no_of_matches(self):
        return f'He played {self.matches} matches'


player1 = CricketStats('Rohit', 'Sharma', 35, 25, 600)
player2 = CricketStats('Virat', 'Kohli', 60, 35, 500)


print(player2.no_of_matches())