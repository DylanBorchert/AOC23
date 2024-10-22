from dotenv import load_dotenv
import os
import requests
from functools import cache
from typing import Any
from timeit import default_timer as timer

load_dotenv()
cookie = os.getenv("SESSION")

session = requests.Session()

if not cookie:
    raise Exception("No cookie found in .env file")


# ensures the site gives us the correct data, and not just a lame "you're not logged in" reponse
requests.utils.add_dict_to_cookiejar(session.cookies, {"session": cookie})


@cache
def get_input_data(self) -> str:
    """Takes a day and returns the input data for that day

    Args:
        day (int): The day to get the input data for

    Returns:
        str: The unparsed input data
    """
    url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
    return session.get(url).text


def submit_answer(data, year, day) -> None:
    response = session.post(
        f"https://adventofcode.com/{year}/day/{day}/answer", data=data)
    handle_submit_response(response)


def submit_data(self) -> None:
    print(self)
    day1Answer = self.part1()
    day2Answer = self.part2()
    page = session.get(
        f"https://adventofcode.com/{self.year}/day/{self.day}")

    numberAnswered = page.text.count(f'Your puzzle answer was <code>')

    match numberAnswered:
        case 0:
            input(
                f"{bcolors.BOLD}Part 1:{bcolors.ENDC} {bcolors.WARNING}Press enter to submit answer: {bcolors.OKGREEN}{day2Answer}{bcolors.ENDC} {bcolors.ENDC}")
            data = {
                'level': '1',
                'answer': day1Answer
            }
            submit_answer(data, self.year, self.day)
        case 1:
            print(
                f"{bcolors.OKGREEN}⭐️ Answer for Part 1 Correct!{bcolors.ENDC}\n")

            input(
                f"{bcolors.BOLD}Part 2:{bcolors.ENDC} {bcolors.WARNING}Press enter to submit answer: {bcolors.OKGREEN}{day2Answer}{bcolors.ENDC} {bcolors.ENDC}")
            data = {
                'level': '2',
                'answer': day2Answer
            }
            submit_answer(data, self.year, self.day)
        case 2:
            print(f"{bcolors.OKGREEN}⭐️ Both Parts Correct!{bcolors.ENDC}")
    return ''


def handle_submit_response(response):
    print()
    if 'You gave an answer too recently' in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print(
            f'{bcolors.BOLD}-= -=-{bcolors.ENDC}{bcolors.FAIL} TOO MANY REQUESTS {bcolors.ENDC}{bcolors.BOLD}-= -=-{bcolors.ENDC}')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print(
                f'{bcolors.BOLD}-= -=-{bcolors.ENDC}{bcolors.FAIL} WRONG (TOO LOW) {bcolors.ENDC}{bcolors.BOLD}-= -=-{bcolors.ENDC}')
        elif 'too high' in response.text:
            print(
                f'{bcolors.BOLD}-= -=-{bcolors.ENDC}{bcolors.FAIL} WRONG (TOO HIGH) {bcolors.ENDC}{bcolors.BOLD}-= -=-{bcolors.ENDC}')
        else:
            print(
                f'{bcolors.BOLD}-= -=-{bcolors.ENDC}{bcolors.FAIL} WRONG {bcolors.ENDC}{bcolors.BOLD}-= -=-{bcolors.ENDC}')
    elif 'seem to be solving the right level.' in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print(
            f"{bcolors.BOLD}-= -=-{bcolors.ENDC}{bcolors.OKGREEN} ALREADY SOLVED {bcolors.ENDC}{bcolors.BOLD}-= -=-{bcolors.ENDC}")
    else:
        print(
            f"{bcolors.BOLD}-= -=-{bcolors.ENDC}{bcolors.OKGREEN} CORRECT! {bcolors.ENDC}{bcolors.BOLD}-= -=-{bcolors.ENDC}")


class Template:
    def __init__(self, day: int, year: int, useFile: bool = False, file_location: str = None):
        """Initializes the template class"""
        self.day = day
        self.year = year
        self.link = f"https://adventofcode.com/{year}/day/{day}"
        if not useFile:
            self.__data = get_input_data(self)
        else:
            if not file_location:
                file_location = f"test.txt"
            f = open(file_location, "r")
            data = f.read()
            f.close()
            self.__data = data

    def get_data(self) -> Any:
        """Gets the data for the day
        WARNING: The data may be any type, as it can be modified by the set_data method

        Returns:
            Any: The data for the day
        """
        return self.__data

    def set_data(self, data: Any) -> None:
        """Sets the data as the given data
        WARNING: The data may be any type

        Args:
            data (Any): The data to set the data to
        """
        self.__data = data

    def submit(self) -> None:
        return submit_data(self)

    def part1(self) -> int:
        """Returns the numerical answer for part 1"""
        pass

    def part2(self) -> int:
        """Returns the numerical answer for part 2"""
        pass

    def __str__(self) -> str:
        """Returns the string representation of the day"""
        newline = "\n"
        return f"{newline * 5}{bcolors.BOLD} -= -=- {bcolors.OKGREEN}ADVENT {bcolors.FAIL}OF {bcolors.OKGREEN}CODE {bcolors.FAIL}DAY {bcolors.OKGREEN}{self.day}{bcolors.ENDC}{bcolors.BOLD} -= -=-{bcolors.ENDC}\n{bcolors.UNDERLINE}{bcolors.OKCYAN}{self.link}{bcolors.ENDC}\n\n{self.get_part1_timing()}\n{self.get_part2_timing()}{newline}"

    def get_part1_timing(self) -> str:
        """Returns the time taken to run part 1"""
        start = timer()
        result = self.part1()
        end = timer()
        return f"{bcolors.BOLD}Part One:{bcolors.ENDC} {bcolors.OKGREEN}{result}{bcolors.ENDC} ({bcolors.OKCYAN}{end - start:.7f}{bcolors.ENDC} seconds)"

    def get_part2_timing(self) -> str:
        """Returns the time taken to run part 2"""
        start = timer()
        result = self.part2()
        end = timer()
        return f"{bcolors.BOLD}Part Two:{bcolors.ENDC} {bcolors.OKGREEN}{result}{bcolors.ENDC} ({bcolors.OKCYAN}{end - start:.7f}{bcolors.ENDC} seconds)"

    def get_total_timing(self) -> float:
        """Returns the time taken to run both parts"""
        return self.get_part1_timing() + self.get_part2_timing()


# from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
