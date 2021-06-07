import random


class NegativeNumberError(Exception):
    pass


class LargerThanMillionError(Exception):
    pass


class Robogotchi:
    def __init__(self, name):
        self.name = name
        self.features = {'battery': 100, 'overheat': 0, 'skill': 0, 'boredom': 0, 'rust': 0}
        self.previous_features = self.features
        self.accidents = {'puddle': 10, 'sprinkler': 30, 'pool': 50, 'lucky': 0}

    def menu(self):
        print(f"Available interactions with {self.name}:\nexit - Exit\ninfo - Check the vitals\nwork - Work\n"
              f"play - Play\noil - Oil\nrecharge - Recharge\nsleep - Sleep mode\nlearn - Learn skills\n")
        choose = input("Choose:\n")
        while choose != "exit":
            if self.features['battery'] == 0 and choose != "recharge":
                print(f"The level of the battery is 0, {self.name} needs recharging!")
            elif self.features['boredom'] >= 100 and choose != "play":
                print(f"{self.name} is too bored! {self.name} needs to have fun!")
            elif choose == "recharge":
                self.recharge()
            elif choose == "play":
                self.play()
            elif choose == "sleep":
                self.sleep()
            elif choose == "info":
                self.info()
            elif choose == "learn":
                self.learn()
            elif choose == "work":
                self.work()
            elif choose == "oil":
                self.oil()
            else:
                print("Invalid input, try again!\n")
            if self.features['overheat'] >= 100:
                print(f"The level of overheat reached 100, {self.name} has blown up! Game over. Try again?")
                break
            if self.features['rust'] >= 100:
                print(f"{self.name} is too rusty! Game over. Try again?")
                break
            print(f"Available interactions with {self.name}:\nexit - Exit\ninfo - Check the vitals\nwork - Work\n"
                  f"play - Play\noil - Oil\nrecharge - Recharge\nsleep - Sleep mode\nlearn - Learn skills\n")
            choose = input("Choose:\n")
        if self.features['overheat'] != 100:
            print("Game over.")

    def info(self):
        print(f"{self.name}'s stats are:\nbattery is {self.features['battery']},\n"
              f"overheat is {self.features['overheat']},\nskill level is {self.features['skill']},\n"
              f"boredom is {self.features['boredom']},\nrust is {self.features['rust']}.\n")

    def play(self):
        games = ['numbers', 'rock-paper-scissors']
        choice = input('Which game would you like to play?').lower()
        while choice not in games:
            choice = input('Please choose a valid option: Numbers or Rock-paper-scissors?')
        if choice == "numbers":
            self.numbers()
        elif choice == "rock-paper-scissors":
            self.rock_paper_scissors()
        accident = self.unpleasant_events()
        self.update_features(boredom=-20, overheat=10, rust=self.accidents[accident])
        self.messages('boredom', 'overheat')
        if accident != 'lucky':
            self.messages('rust')
        if self.features['boredom'] == 0:
            print(f"{self.name} is in a great mood!\n")

    @staticmethod
    def numbers():
        wins = {'player': 0, 'robot': 0, 'draws': 0}
        player = input("What is your number?\n")
        while player != "exit game":
            goal_number = random.randint(0, 1000000)
            robot = random.randint(0, 1000000)
            try:
                player = int(player)
                if player < 0:
                    raise NegativeNumberError
                elif player > 1000000:
                    raise LargerThanMillionError
                else:
                    print(f"The robot entered the number {robot}.\nThe goal number is {goal_number}.")
                    if abs(goal_number - robot) < abs(goal_number - player):
                        print("The robot won!")
                        wins['robot'] += 1
                    elif abs(goal_number - robot) > abs(goal_number - player):
                        print("You won!")
                        wins['player'] += 1
                    else:
                        print("It's a draw!")
                        wins['draws'] += 1
            except ValueError:
                print("A string is not a valid input!")
            except NegativeNumberError:
                print("The number can't be negative!")
            except LargerThanMillionError:
                print("Invalid input! The number can't be bigger than 1000000")
            player = input("What is your number?\n")
        print(f"You won: {wins['player']},\nRobot won: {wins['robot']},\nDraws: {wins['draws']}.\n")

    @staticmethod
    def rock_paper_scissors():
        options = ["paper", "rock", "scissors"]
        beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        wins = {'player': 0, 'robot': 0, 'draws': 0}
        player = input("What is your move?\n")
        while player != "exit game":
            robot = random.choice(options)
            if player in options:
                print(f"The robot chose {robot}.")
                if player == robot:
                    print("It's a draw!")
                    wins['draws'] += 1
                elif beats[player] == robot:
                    print("You won!")
                    wins['player'] += 1
                elif beats[robot] == player:
                    print("The robot won!")
                    wins['robot'] += 1
            else:
                print("No such option! Try again!")
            player = input("What is your move?\n")
        print(f"You won: {wins['player']},\nRobot won: {wins['robot']},\nDraws: {wins['draws']}.\n")

    def recharge(self):
        if self.features['battery'] == 100:
            print(f"{self.name} is charged!\n")
        else:
            self.update_features(battery=10, overheat=-5, boredom=5)
            self.messages('overheat', 'battery', 'boredom')
            print(f"{self.name} is recharged!")

    def sleep(self):
        if self.features['overheat'] == 0:
            print(f"{self.name} is cool!\n")
        else:
            self.update_features(overheat=-20)
            print(f"{self.name} cooled off!\n")
            self.messages('overheat')
            if self.features['overheat'] == 0:
                print(f"{self.name} is cool!\n")

    def update_features(self, battery=0, overheat=0, skill=0, boredom=0, rust=0):
        self.previous_features = self.features.copy()
        self.features['boredom'] += boredom
        self.features['overheat'] += overheat
        self.features['skill'] += skill
        self.features['battery'] += battery
        self.features['rust'] += rust

        for attribute in self.features:
            if self.features[attribute] < 0:
                self.features[attribute] = 0

    def learn(self):
        if self.features['skill'] == 100:
            print(f"There's nothing for {self.name} to learn!\n")
        else:
            self.update_features(boredom=5, overheat=10, skill=10, battery=-10)
            self.messages('skill', 'overheat', 'battery', 'boredom')
            print(f"{self.name} has become smarter!\n")

    def work(self):
        if self.features['skill'] < 50:
            print(f"{self.name} has got to learn before working!\n")
        else:
            accident = self.unpleasant_events()
            self.update_features(boredom=10, overheat=10, battery=-10, rust=self.accidents[accident])
            self.messages('overheat', 'boredom', 'battery')
            if accident != 'lucky':
                self.messages('rust')
            print(f"{self.name} did well!\n")

    def unpleasant_events(self):
        accident = random.choice(['puddle', 'sprinkler', 'pool', 'lucky'])
        if accident == 'puddle':
            print(f"Oh no, {self.name} stepped into a puddle!\n")
        elif accident == 'sprinkler':
            print(f"Oh, {self.name} encountered a sprinkler!\n")
        elif accident == 'pool':
            print(f"Guess what! {self.name} fell into the pool!\n")
        return accident

    def oil(self):
        if self.features['rust'] == 0:
            print(f"{self.name} is fine, no need to oil!\n")
        else:
            self.update_features(rust=-20)
            self.messages('rust')
            print(f"{self.name} is less rusty!\n")

    def messages(self, *features):
        for attribute in features:
            print(f"{self.name}'s level of {'the ' if attribute == 'battery' else ''}{attribute} was "
                  f"{self.previous_features[attribute]}. Now it is {self.features[attribute]}.")


robopet = Robogotchi(input("How will you call your robot?\n"))
robopet.menu()
