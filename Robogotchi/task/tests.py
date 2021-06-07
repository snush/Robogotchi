from typing import List, Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from hstest.exceptions import WrongAnswerException


class RobogotchiTestParent(StageTest):


    def prs_print_check(self, output, answer):
        parsed_output = output.split()[:-4]
        try:
            robot_answer = parsed_output[2] if parsed_output[1] == 'chose' else parsed_output[3]
            ideal = self.check_who_won_ro(robot_answer=robot_answer,
                                          human_answer=answer).split('\n')
            ideal = [line for line in ideal if line]
            for i in ideal:
                if i.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                               f"{i}")
            return True
        except IndexError:
            pass

    def check_who_won_num(self, human_answer, robot_answer, goal):
        if abs(goal - human_answer) < abs(goal - robot_answer):
            self.won_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nYou won!")
        elif abs(goal - human_answer) > abs(goal - robot_answer):
            self.lost_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nRobot won!")
        else:
            self.draw_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nIt's a draw!")

    def check_who_won_ro(self, human_answer, robot_answer):
        if human_answer == 'paper':
            if robot_answer == 'scissors':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'rock':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        elif human_answer == 'rock':
            if robot_answer == 'paper':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'scissors':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        elif human_answer == 'scissors':
            if robot_answer == 'rock':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'paper':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        else:
            return 'No such option! Try again!\n'

    def interface_prints_check(self, output):
        interface_parsed = self.ideal_interface.split('\n')
        output = output.lower()
        for inter in interface_parsed:
            if inter.lower().strip() not in output:
                raise WrongAnswerException(f"The following string is not found in your menu output:\n"
                                           f"{inter}")
        return True

    def oil_what_prints(self, output):
        if (self.rust == 0) and ('fine' in output):
            if "Daneel is fine, no need to oil" not in output:
                return False
        elif self.boredom == 100:
            if "Daneel is too bored" not in output:
                return False
        else:
            i = 10 if 'was 10' in output else 20
            text = f"Daneel's level of rust was {self.rust+i}. Now it is {self.rust}." \
                   f"\nDaneel is less rusty"
            text = text.split('\n')
            for tex in text:
                if tex.lower().strip() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def recharge_what_prints(self, output):
        if self.battery == 100 and 'level' not in output:
            if "Daneel is charged" not in output:
                return False
        else:
            if self.battery != 100:
                message = '\nDaneel is recharged'
                text = f"Daneel's level of overheat was {self.overheat+5}. Now it is {self.overheat}." \
                                f"\nDaneel's level of the battery was {self.battery-10}. Now it is {self.battery}." \
                                f"\nDaneel's level of boredom was {self.boredom-5}. Now it is {self.boredom}.\n" \
                                f"{message}"
                text = text.split('\n')
                for tex in text:
                    if tex.lower() not in output.lower():
                        raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def sleep_what_prints(self, output):
        if self.overheat == 0:
            if "Daneel is cool" not in output:
                return False
        else:
            if self.overheat != 0:
                insertion  = '\nDaneel cooled off'
            else:
                insertion = '\nDaneel is cool'
            text = f"Daneel's level of overheat was {self.overheat + 20}. Now it is {self.overheat}.\n" \
                   f"{insertion}"
            text = text.split('\n')
            for tex in text:
                if tex.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def learn_changes(self, output):
        if self.skills != 100:
            text = f"Daneel's level of skill was {self.skills-10}. Now it is {self.skills}." \
                   f"\nDaneel's level of overheat was {self.overheat-10}. Now it is {self.overheat}." \
                   f"\nDaneel's level of the battery was {self.battery+10}. Now it is {self.battery}." \
                   f"\nDaneel's level of boredom was {self.boredom-5}. Now it is {self.boredom}." \
                   f"\n\nDaneel has become smarter!".split('\n')
            for tex in text:
                if tex.lower().strip() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def game_statistics_prints_check(self, output, game):
        if game == 'numbers':
            ideal = f"You won: {self.won_numbers}," \
                    f"\nRobot won: {self.lost_numbers}," \
                    f"\nDraws: {self.draw_numbers}."
            ideal = ideal.split('\n')
            for i in ideal:
                if i.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                               f"{i}")
        else:
            ideal = f"You won: {self.won_roshambo}," \
                    f"\nRobot won: {self.lost_roshambo}," \
                    f"\nDraws: {self.draw_roshambo}."
            ideal = ideal.split('\n')
            for i in ideal:
                if i.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                               f"{i}")
        return True

    def increase_the_params(self, command):
        if command == 'learn':
            self.skills += 10
            self.overheat = self.overheat + 10 if self.overheat + 10 <= 100 else 100
            self.battery = self.battery - 10 if self.battery - 10 > 0 else 0
            self.boredom = self.boredom + 5 if self.boredom + 5 < 100 else 100
        elif command == 'play':
            self.boredom = self.boredom - 20 if self.boredom - 20 >= 0 else self.boredom - self.boredom
            self.overheat = self.overheat + 10 if self.overheat + 10 < 100 else 100
        elif command == 'work':
            self.boredom = self.boredom + 10 if self.boredom + 10 < 100 else 100
            self.overheat = self.overheat + 10 if self.overheat + 10 < 100 else 100
            self.battery = self.battery - 10 if self.battery - 10 > 0 else 0
        elif command == 'oil':
            self.rust = self.rust - 20 if self.rust - 20 > 0 else self.rust-self.rust
        elif command == 'sleep':
            self.overheat = self.overheat - 20 if self.overheat - 20 > 0 else self.overheat-self.overheat
        elif command == 'recharge':
            self.overheat = self.overheat - 5 if self.overheat - 5 > 0 else 0
            self.battery = self.battery + 10 if self.battery + 10 < 100 else 100
            self.boredom = self.boredom + 5 if self.boredom + 5 < 100 else 100

    def get_the_rust(self, output):
        if 'puddle' in output:
            return 10
        elif 'sprinkler' in output:
            return 30
        elif 'pool' in output:
            return 50
        return 0


    def play_what_prints_check(self, output):
        if "which game would you like to play?" not in output.lower():
            return False
        return True

    def roshambo_what_prints_check(self, output):
        if "what is your move?" not in output.lower():
            return False
        return True

    def work_what_prints(self, output):
        if self.skills < 50:
            if 'Daneel has got to learn before working' not in output:
                return False
        return True

    def wrong_option_what_prints(self, output):
        check = "invalid input" in output.lower() and 'try again' in output.lower()
        if not check:
            return False
        return True

    def check_the_rust_output(self, output, action):
        if action == 'play':
            some_rust = f"\nDaneel's level of overheat was {self.overheat-10}. Now it is {self.overheat}." \
                               f"\nDaneel's level of boredom was {self.boredom_previous}. Now it is {self.boredom}."
            boredom_str = f"\nDaneel's level of boredom was {self.boredom_previous}. Now it is {self.boredom}."
            rust_dict = {0: '', 10: f"\nOh no, Daneel stepped into a puddle",
                         30: '\nOh, Daneel encountered a sprinkler', 50: '\nGuess what! Daneel fell into the pool'}
            if self.boredom_previous == 0:
                some_rust = some_rust.replace(boredom_str, '')
            if self.boredom == 0:
                some_rust += "\nDaneel is in a great mood"
            if self.get_the_rust(output) > 0:
                some_rust += f"\nDaneel's level of rust was {self.rust_previous}. Now it is {self.rust}"
                some_rust += rust_dict[self.get_the_rust(output)]
            for line in some_rust.split('\n'):
                if line.lower().strip() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{line}")
            return True
        elif action == 'work':
            some_rust = f"Daneel's level of boredom was {self.boredom-10}. Now it is {self.boredom}." \
                      f"\nDaneel's level of overheat was {self.overheat-10}. Now it is {self.overheat}." \
                      f"\nDaneel's level of the battery was {self.battery+10}. Now it is {self.battery}." \
                      f"\n\nDaneel did well!"
            rust_dict = {0: '', 10: f"\nOh no, Daneel stepped into a puddle",
                         30: '\nOh, Daneel encountered a sprinkler', 50: '\nGuess what! Daneel fell into the pool'}
            if self.get_the_rust(output) > 0:
                some_rust += f"\nDaneel's level of rust was {self.rust_previous}. Now it is {self.rust}"
                some_rust += rust_dict[self.get_the_rust(output)]
            for line in some_rust.split('\n'):
                if line.lower().strip() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{line}")
            return True

    def info_what_prints(self, output):
        text = f"Daneel's stats are:" \
               f"\nbattery is {self.battery}," \
               f"\noverheat is {self.overheat}," \
               f"\nskill level is {self.skills}," \
               f"\nboredom is {self.boredom}," \
               f"\nrust is {self.rust}."
        text = text.split('\n')
        for tex in text:
            if tex.strip().lower() not in output.lower():
                raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def parse_the_output(self, output):
        parsed_output = output.split()
        check = len(parsed_output) >= 11 and isinstance(int(parsed_output[5].strip('.')), int) \
                and isinstance(int(parsed_output[10].strip('.')), int)
        if not check:
            raise WrongAnswerException("The result of the game is formatted incorrectly")
        else:
            robot_answer = int(parsed_output[5].strip('.'))
            goal_number = int(parsed_output[10].strip('.'))
        return robot_answer, goal_number

    def normal_number_prints_check(self, output, number):
        try:
            parsed_output = output.split()
            robot_answer = int(parsed_output[5].strip('.'))
            goal_number = int(parsed_output[10].strip('.'))
            ideal = self.check_who_won_num(number, robot_answer, goal_number).split('\n')
            ideal = [line for line in ideal if line][-1]
            if ideal.lower() not in output.lower():
                raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                           f"{ideal}")
            return True
        except ValueError:
            return False

    def numbers_what_prints_check(self, output):
        if 'what is your number?' not in output.lower():
            return False
        return True

    def numbers_exceptions(self, output, kind):
        output = [line for line in output.lower().split('\n') if line][0]
        if isinstance(kind, str):
            if "a string is not a valid input" not in output:
                return False
        elif kind > 1000000:
            if "the number can't be bigger than 1000000" not in output:
                return False
        elif kind < 0:
            if "number can't be negative" not in output:
                return False
        return True

    def knife_exception(self, output):
        check = 'no such option' in output.lower() and 'try again' in output.lower()
        if not check:
            return False
        return True

    def zerify_numbers_count(self, game):
        if game == 'numbers':
            self.won_numbers = 0
            self.lost_numbers = 0
            self.draw_numbers = 0
        else:
            self.won_roshambo = 0
            self.lost_roshambo = 0
            self.draw_roshambo = 0

    def fresh_start(self):
        self.skills = 0
        self.overheat = 0
        self.boredom = 0
        self.battery = 100
        self.rust = 0

        self.boredom_previous = 0
        self.rust_previous = 0


class RobogotchiTest1(RobogotchiTestParent):

    ideal_interface = "\nAvailable interactions with Daneel:" \
                      "\nexit\ninfo" \
                      "\nwork" \
                      "\nplay" \
                      "\noil" \
                      "\nrecharge" \
                      "\nsleep" \
                      "\nlearn\n" \
                      "\nChoose:"

    won_roshambo = 0
    lost_roshambo = 0
    draw_roshambo = 0

    won_numbers = 0
    lost_numbers = 0
    draw_numbers = 0

    skills = 0
    overheat = 0
    boredom = 0
    battery = 100
    rust = 0

    boredom_previous = 0
    rust_previous = 0

    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin=[self.func1, self.func2, self.func3, self.func4, self.func5, self.func6, self.func7]),
            TestCase(stdin=[self.func8, self.func9, self.func10, self.func11, self.func12, self.func13, self.func14,
                            self.func15, self.func16, self.func17]),
            TestCase(stdin=[self.func18, self.func19, self.func20, self.func21, self.func22, self.func23, self.func24,
                            self.func25, self.func26, self.func27, self.func28, self.func29, self.func30, self.func31,
                            self.func32, self.func33, self.func34]),
            TestCase(stdin=[self.func35, self.func36, self.func37, self.func38, self.func39, self.func40, self.func41,
                            self.func42, self.func43, self.func44, self.func45, self.func46, self.func47, self.func48,
                            self.func49, self.func50, self.func51, self.func52, self.func53, self.func54, self.func55,
                            self.func56, self.func57, self.func58, self.func59, self.func60, self.func61, self.func62,
                            self.func63, self.func64, self.func65, self.func66, self.func67, self.func68, self.func69,
                            self.func70, self.func71, self.func72, self.func73, self.func74, self.func75, self.func76,
                            self.func77, self.func78, self.func79, self.func80]),
            TestCase(stdin=[self.func81, self.func82, self.func83, self.func84, self.func85, self.func86, self.func87,
                            self.func88, self.func89, self.func90, self.func91, self.func92, self.func93, self.func94],
                     check_function=self.check_boom),
            TestCase(stdin=[self.func95, self.func96, self.func97, self.func98, self.func99, self.func100, self.func101,
                            self.func102, self.func103, self.func104, self.func105, self.func106, self.func107,
                            self.func108, self.func109, self.func110, self.func111, self.func112, self.func113,
                            self.func114, self.func115, self.func116, self.func117, self.func118, self.func119,
                            self.func120, self.func121, self.func122, self.func123, self.func124, self.func125,
                            self.func126, self.func127, self.func128, self.func129, self.func130, self.func131,
                            self.func132, self.func133, self.func134, self.func135, self.func136, self.func137,
                            self.func138, self.func139, self.func140], check_function=self.check_rust),
            TestCase(stdin=[self.func141, self.func142, self.func143, self.func144, self.func145, self.func146,
                            self.func147, self.func148, self.func149, self.func150, self.func151, self.func152,
                            self.func153, self.func154, self.func155, self.func156, self.func157, self.func158,
                            self.func159, self.func160, self.func161, self.func162], check_function=self.check_rust)
        ]

    """Test 1"""

    def func1(self, output):
        if output.strip() != 'How will you call your robot?':
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func2(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'info'

    def func3(self, output):
        if not self.info_what_prints(output):
            return CheckResult.wrong("The information provided is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'oil'

    def func4(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The program should print that the robot doesn't need oiling")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'recharge'

    def func5(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The program should print that the robot is charged")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'sleep'

    def func6(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The program should print that the robot is cool")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func7(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'exit'

    """Test 2"""

    def func8(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func9(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func10(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The stats message is incorrect")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        return 'play'

    def func11(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should ask the user which game to play")
        return 'rock-paper-scissors'

    def func12(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'paper'

    def func13(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func14(self, output):
        self.rust += self.get_the_rust(output)
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.check_the_rust_output(output, 'play'):
            return CheckResult.wrong("You printed a wrong message")
        self.zerify_numbers_count('roshambo')
        self.rust_previous = self.rust
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'work'

    def func15(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong("The user should be informed that the robot needs to learn")
        return 'fly to the moon'

    def func16(self, output):
        if not self.wrong_option_what_prints(output):
            return CheckResult.wrong("The user should be informed about incorrect input")
        self.increase_the_params('learn')
        return 'learn'

    def func17(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The stats message is incorrect")
        return 'exit'

    """Test 3"""

    def func18(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func19(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func20(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func21(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func22(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func23(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func24(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func25(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one.")
        self.increase_the_params('oil')
        return 'oil'

    def func26(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one.")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func27(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one.")
        self.increase_the_params('learn')
        return 'learn'

    def func28(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('sleep')
        return 'sleep'

    def func29(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func30(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func31(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'learn'

    def func32(self, output):
        if 'the level of the battery is 0, daneel needs recharging' not in output.lower():
            return CheckResult.wrong("The robot must have run out of the battery by now")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'sleep'

    def func33(self, output):
        if 'the level of the battery is 0, daneel needs recharging' not in output.lower():
            return CheckResult.wrong("The robot must have run out of the battery by now")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func34(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'exit'

    """Test 4"""

    def func35(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func36(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func37(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func38(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func39(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func40(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func41(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func42(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func43(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func44(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func45(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func46(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('sleep')
        return 'sleep'

    def func47(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func48(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func49(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func50(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func51(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func52(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func53(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func54(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func55(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func56(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('sleep')
        return 'sleep'

    def func57(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func58(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func59(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func60(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'oil'

    def func61(self, output):
        if 'daneel is too bored! daneel needs to have fun' not in output.lower():
            return CheckResult.wrong("The robot should be too bored by now. \n"
                                     "The robot shouldn't accept any other actions but \'play\'.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'learn'

    def func62(self, output):
        if 'daneel is too bored! daneel needs to have fun' not in output.lower():
            return CheckResult.wrong("The robot should be too bored by now. \n"
                                     "The robot shouldn't accept any other actions but \'play\'.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'recharge'

    def func63(self, output):
        if 'daneel is too bored! daneel needs to have fun' not in output.lower():
            return CheckResult.wrong("The robot should be too bored by now. \n"
                                     "The robot shouldn't accept any other actions but \'play\'.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'sleep'

    def func64(self, output):
        if 'daneel is too bored! daneel needs to have fun' not in output.lower():
           return CheckResult.wrong("The robot should be too bored by now. \n"
                                     "The robot shouldn't accept any other actions but \'play\'.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        return 'play'

    def func65(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'rock-paper-scissors'

    def func66(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func67(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func68(self, output):
        self.rust += self.get_the_rust(output)
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.check_the_rust_output(output, 'play'):
            return CheckResult.wrong("You printed a wrong message")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func69(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func70(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'info'

    def func71(self, output):
        if not self.info_what_prints(output):
            return CheckResult.wrong("The information is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func72(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func73(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func74(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        return 'play'

    def func75(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'numbers'

    def func76(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '797'

    def func77(self, output):
        if not self.normal_number_prints_check(output, 797):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'exit game'

    def func78(self, output):
        self.rust += self.get_the_rust(output)
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.check_the_rust_output(output, 'play'):
            return CheckResult.wrong("You printed a wrong message")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func79(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'learn'

    def func80(self, output):
        if "there's nothing for daneel to learn" not in output.lower():
            return CheckResult.wrong("The robot should be the cleverest by now")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'exit'

    """Test 5"""

    def func81(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func82(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func83(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func84(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func85(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func86(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func87(self, output): # чекни
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func88(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('work')
        return 'work'

    def func89(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func90(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('oil')
        return 'oil'

    def func91(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        self.increase_the_params('learn')
        return 'learn'

    def func92(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func93(self, output):
        self.rust += self.get_the_rust(output)
        if not self.check_the_rust_output(output, 'work'):
            return CheckResult.wrong("The parameters weren't changed correctly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func94(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    """Test 6"""

    def func95(self, output):
        self.fresh_start()
        self.zerify_numbers_count('numbers')
        self.zerify_numbers_count('roshambo')
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func96(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        return 'play'

    def func97(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'numbers'

    def func98(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '457'

    def func99(self, output):
        if not self.normal_number_prints_check(output, 457):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'chamesh'

    def func100(self, output):
        if not self.numbers_exceptions(output, 'chamesh'):
            return CheckResult.wrong("The program should inform the user about invalid input")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'exit game'

    def func101(self, output):
        self.rust += self.get_the_rust(output)
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.check_the_rust_output(output, 'play'):
            return CheckResult.wrong("You printed a wrong message")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        self.zerify_numbers_count('numbers')
        return 'play'

    def func102(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'rock-paper-scissors'

    def func103(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'scissors'

    def func104(self, output):
        if not self.prs_print_check(output, 'scissors'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'pen'

    def func105(self, output):
        if not self.knife_exception(output):
            return CheckResult.wrong("The program should inform the user about invalid input")
        return 'exit game'

    def func106(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'roshambo'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('roshambo')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func107(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'u-95'

    def func108(self, output):
        if "please choose a valid option: numbers or rock-paper-scissors?" not in output.lower():
            return CheckResult.wrong("The user should be informed about an invalid choice")
        return 'numbers'

    def func109(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '13579'

    def func110(self, output):
        if not self.normal_number_prints_check(output, 13579):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '5000003'

    def func111(self, output):
        if not self.numbers_exceptions(output, 5000003):
            return CheckResult.wrong("The program should inform the user about invalid input")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '77921'

    def func112(self, output):
        if not self.normal_number_prints_check(output, 77921):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '9'

    def func113(self, output):
        if not self.normal_number_prints_check(output, 9):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func114(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'numbers'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('numbers')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func115(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'rock-paper-scissors'

    def func116(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func117(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'paper'

    def func118(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'scissors'

    def func119(self, output):
        if not self.prs_print_check(output, 'scissors'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        return 'exit game'

    def func120(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'roshambo'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('roshambo')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func121(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'numbers'

    def func122(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '999999'

    def func123(self, output):
        if not self.normal_number_prints_check(output, 999999):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func124(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'numbers'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('numbers')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func125(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'rock-paper-scissors'

    def func126(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func127(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func128(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'roshambo'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('roshambo')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func129(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'numbers'

    def func130(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '27'

    def func131(self, output):
        if not self.normal_number_prints_check(output, 27):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func132(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'numbers'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('numbers')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func133(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'rock-paper-scissors'

    def func134(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'paper'

    def func135(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func136(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'roshambo'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('roshambo')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'play'

    def func137(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'numbers'

    def func138(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '435679'

    def func139(self, output):
        if not self.normal_number_prints_check(output, 435679):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        return 'exit game'

    def func140(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.game_statistics_prints_check(output, 'numbers'):
                return CheckResult.wrong("The statistics is incorrect")
            if not self.check_the_rust_output(output, 'play'):
                return CheckResult.wrong("You printed a wrong message")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.zerify_numbers_count('numbers')
            self.boredom_previous = self.boredom
            self.rust_previous = self.rust
            self.increase_the_params('play')
        return 'exit'

    """Test 7"""

    def func141(self, output):
        self.fresh_start()
        self.zerify_numbers_count('numbers')
        self.zerify_numbers_count('roshambo')
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func142(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func143(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func144(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func145(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func146(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func147(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        return 'play'

    def func148(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'rock-paper-scissors'

    def func149(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'scissors'

    def func150(self, output):
        if not self.prs_print_check(output, 'scissors'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func151(self, output):
        self.rust += self.get_the_rust(output)
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.check_the_rust_output(output, 'play'):
            return CheckResult.wrong("You printed a wrong message")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func152(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.rust_previous = self.rust
            self.increase_the_params('work')
        return 'work'

    def func153(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.increase_the_params('recharge')
        return 'recharge'

    def func154(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The program should print that the robot is charged")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func155(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.increase_the_params('sleep')
        return 'sleep'

    def func156(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('sleep')
        return 'sleep'

    def func157(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func158(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.rust_previous = self.rust
            self.increase_the_params('work')
        return 'work'

    def func159(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.rust_previous = self.rust
            self.increase_the_params('recharge')
        return 'recharge'

    def func160(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func161(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.rust_previous = self.rust
            self.increase_the_params('work')
        return 'work'

    def func162(self, output):
        self.rust += self.get_the_rust(output)
        if self.rust >= 100:
            if output[-10:] != "Daneel is too rusty! Game over. Try again?":
                return CheckResult.wrong("The robot should be too rusty by now")
        else:
            if not self.check_the_rust_output(output, 'work'):
                return CheckResult.wrong("The parameters weren't changed correctly.")
            if not self.interface_prints_check(output):
                return CheckResult.wrong("The interface is different from the exemplary one")
            self.rust_previous = self.rust
            self.increase_the_params('work')

    def check(self, reply: str, attach: Any) -> CheckResult:
        if 'game over' not in reply.lower():
            return CheckResult.wrong("The program should print that the game is over")
        return CheckResult.correct()


    def check_boom(self, reply: str, attach: Any) -> CheckResult:
        check = 'the level of overheat reached 100, daneel has blown up' in reply.lower()
        check2 = 'game over' in reply.lower() and 'try again?' in reply.lower()
        if not (check and check2):
            return CheckResult.wrong("The program should print that the game is over")
        return CheckResult.correct()

    def check_rust(self, reply: str, attach: Any) -> CheckResult:
        check = 'daneel is too rusty' in reply.lower() and 'game over' in reply.lower() and 'try again?' in reply.lower()
        if not check:
            return CheckResult.wrong("The robot should be too rusty by now")
        return CheckResult.correct()


if __name__ == '__main__':
    RobogotchiTest1('robogotchi.robogotchi').run_tests()

